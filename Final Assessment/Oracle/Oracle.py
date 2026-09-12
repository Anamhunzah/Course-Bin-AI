import os
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import TimeSeriesSplit
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, ExtraTreesClassifier, IsolationForest
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

STOCK='Oracle'
BASE=Path(__file__).resolve().parent
DATA=BASE/'oracle.csv'
OUT=BASE/f'{STOCK}_results'
CHARTS=OUT/'charts'; TABLES=OUT/'tables'
CHARTS.mkdir(parents=True,exist_ok=True); TABLES.mkdir(parents=True,exist_ok=True)
sns.set_theme(style='whitegrid')

def load_stock(path):
    df=pd.read_csv(path)
    df['Date']=pd.to_datetime(df['Date'],errors='coerce',utc=True).dt.tz_convert(None)
    df=df.dropna(subset=['Date']).sort_values('Date').drop_duplicates('Date')
    cols=[c for c in ['Date','Open','High','Low','Close','Volume'] if c in df.columns]
    df=df[cols].copy()
    for c in cols[1:]: df[c]=pd.to_numeric(df[c],errors='coerce')
    df=df.dropna(subset=['Close']); df=df[df['Close']>0]
    return df.set_index('Date')

def features(df):
    x=df.copy()
    x['Return']=x['Close'].pct_change(); x['Log_Return']=np.log(x['Close']/x['Close'].shift(1))
    x['Year']=x.index.year; x['Month']=x.index.month; x['Quarter']=x.index.quarter; x['Day']=x.index.dayofweek
    for w in [20,50,100,200]: x[f'MA{w}']=x['Close'].rolling(w).mean()
    for w in [5,10,20,60]: x[f'Vol{w}']=x['Return'].rolling(w).std()
    x['Mom5']=x['Close']/x['Close'].shift(5)-1; x['Mom20']=x['Close']/x['Close'].shift(20)-1
    x['Volume_Ratio']=x['Volume']/x['Volume'].rolling(20).mean(); x['HL_Range']=(x['High']-x['Low'])/x['Close']; x['Gap']=(x['Open']-x['Close'].shift(1))/x['Close'].shift(1)
    delta=x['Close'].diff(); gain=delta.clip(lower=0).rolling(14).mean(); loss=(-delta.clip(upper=0)).rolling(14).mean(); rs=gain/loss.replace(0,np.nan); x['RSI']=100-100/(1+rs)
    e12=x['Close'].ewm(span=12,adjust=False).mean(); e26=x['Close'].ewm(span=26,adjust=False).mean(); x['MACD']=e12-e26; x['MACD_Signal']=x['MACD'].ewm(span=9,adjust=False).mean()
    prev=x['Close'].shift(1); tr=pd.concat([x['High']-x['Low'],(x['High']-prev).abs(),(x['Low']-prev).abs()],axis=1).max(axis=1); x['ATR']=tr.rolling(14).mean()
    lo=x['Low'].rolling(14).min(); hi=x['High'].rolling(14).max(); x['Stochastic_K']=100*(x['Close']-lo)/(hi-lo).replace(0,np.nan)
    x['OBV']=(np.sign(x['Close'].diff()).fillna(0)*x['Volume']).cumsum()
    x['Regime']=np.select([(x['MA20']>x['MA50'])&(x['Vol20']<=x['Vol60']),(x['MA20']<x['MA50'])&(x['Vol20']>x['Vol60']),x['MA20']>x['MA50'],x['MA20']<x['MA50']],['Bull / Normal','Bear / High Vol','Bull / High Vol','Bear / Normal'],default='Mixed')
    x['Tomorrow_Return']=x['Close'].shift(-1)/x['Close']-1; x['Target']=(x['Tomorrow_Return']>0).astype(int)
    return x

# 1 Load data
print('\n'+'='*72); print(f'{STOCK} — FINAL ASSESSMENT'); print('='*72)
df=load_stock(DATA)
print('Shape:',df.shape); print('Date range:',df.index.min().date(),'to',df.index.max().date())

# 2 Validation
validation=pd.DataFrame({'Metric':['Rows','Columns','Missing Values','Duplicate Dates','Minimum Close','Maximum Close'],'Value':[len(df),len(df.columns),int(df.isna().sum().sum()),int(df.index.duplicated().sum()),df['Close'].min(),df['Close'].max()]})
print('\nSTEP 2 — DATA VALIDATION'); print(validation.to_string(index=False)); validation.to_csv(TABLES/f'{STOCK}_01_validation.csv',index=False)

# 3 Descriptive statistics
desc=df.describe().T; print('\nSTEP 3 — DESCRIPTIVE STATISTICS'); print(desc.round(4)); desc.to_csv(TABLES/f'{STOCK}_02_descriptive_statistics.csv')

# 4 NumPy research
ret=df['Close'].pct_change().dropna(); arr=ret.to_numpy(); cum=np.cumprod(1+arr); peak=np.maximum.accumulate(cum); dd=(cum-peak)/peak
years=max((df.index[-1]-df.index[0]).days/365.25,1/365.25); cagr=(df['Close'].iloc[-1]/df['Close'].iloc[0])**(1/years)-1
risk=pd.DataFrame({'Metric':['Maximum Close','Maximum Volume','Average Daily Return','Maximum Daily Return','Minimum Daily Return','Annualized Volatility','CAGR','Maximum Drawdown','Annualized Sharpe'],'Value':[df['Close'].max(),df['Volume'].max(),ret.mean(),ret.max(),ret.min(),ret.std()*np.sqrt(252),cagr,dd.min(),ret.mean()/ret.std()*np.sqrt(252)]})
print('\nSTEP 4 — NUMPY / RISK SUMMARY'); print(risk.round(6).to_string(index=False)); risk.to_csv(TABLES/f'{STOCK}_03_numpy_risk_summary.csv',index=False)

# 5 Pandas feature engineering
data=features(df); data.to_csv(TABLES/f'{STOCK}_04_engineered_data.csv')
print('\nSTEP 5 — FEATURE ENGINEERING COMPLETE:',len(data.columns),'columns')

# 6 Seaborn / visualization
plt.figure(figsize=(11,4)); plt.plot(data.index,data['Close']); plt.title(f'{STOCK} Closing Price'); plt.tight_layout(); plt.savefig(CHARTS/f'{STOCK}_01_closing_price.png',dpi=130); plt.close()
plt.figure(figsize=(11,4)); plt.plot(data.index,data['Close'],label='Close'); plt.plot(data.index,data['MA20'],label='MA20'); plt.plot(data.index,data['MA50'],label='MA50'); plt.title(f'{STOCK} Price + Moving Averages'); plt.legend(); plt.tight_layout(); plt.savefig(CHARTS/f'{STOCK}_02_moving_averages.png',dpi=130); plt.close()
plt.figure(figsize=(10,4)); plt.hist(data['Return'].dropna(),bins=60); plt.title(f'{STOCK} Return Distribution'); plt.xlabel('Daily Return'); plt.tight_layout(); plt.savefig(CHARTS/f'{STOCK}_03_return_distribution.png',dpi=130); plt.close()
cols=['Close','Return','Volume','Vol20','Mom20','RSI','MACD','Volume_Ratio','HL_Range','ATR']
plt.figure(figsize=(10,7)); sns.heatmap(data[cols].corr(),annot=True,fmt='.2f',cmap='coolwarm'); plt.title(f'{STOCK} Correlation Heatmap'); plt.tight_layout(); plt.savefig(CHARTS/f'{STOCK}_04_correlation_heatmap.png',dpi=130); plt.close()
plt.figure(figsize=(9,4)); sns.boxplot(x='Regime',y='Return',data=data); plt.title(f'{STOCK} Returns by Market Regime'); plt.xticks(rotation=15); plt.tight_layout(); plt.savefig(CHARTS/f'{STOCK}_05_regime_boxplot.png',dpi=130); plt.close()

# 7 Statistical research
monthly=data.groupby('Month')['Return'].agg(['mean','std','count']); weekday=data.groupby('Day')['Return'].agg(['mean','std','count']); regime=data.groupby('Regime')['Return'].agg(['mean','std','count'])
monthly.to_csv(TABLES/f'{STOCK}_05_monthly_effect.csv'); weekday.to_csv(TABLES/f'{STOCK}_06_weekday_effect.csv'); regime.to_csv(TABLES/f'{STOCK}_07_regime_statistics.csv')
print('\nSTEP 7 — STATISTICAL RESEARCH'); print('Monthly effect:'); print(monthly.round(4)); print('Regime effect:'); print(regime.round(4))

# 8 Scikit-learn classification
fcols=['MA20','MA50','Mom5','Mom20','Vol20','Vol60','Volume_Ratio','HL_Range','Gap','RSI','MACD','MACD_Signal','ATR','Stochastic_K']
ml=data[fcols+['Target']].dropna(); X=ml[fcols]; y=ml['Target']
models={'Logistic Regression':Pipeline([('scale',StandardScaler()),('model',LogisticRegression(max_iter=1200))]),'Random Forest':RandomForestClassifier(n_estimators=120,max_depth=8,min_samples_leaf=5,random_state=42,n_jobs=-1),'Gradient Boosting':GradientBoostingClassifier(random_state=42),'Extra Trees':ExtraTreesClassifier(n_estimators=120,max_depth=8,min_samples_leaf=5,random_state=42,n_jobs=-1)}
rows=[]
for name,model in models.items():
    actual=[]; pred=[]
    for tr,te in TimeSeriesSplit(n_splits=4).split(X):
        model.fit(X.iloc[tr],y.iloc[tr]); p=model.predict(X.iloc[te]); actual.extend(y.iloc[te]); pred.extend(p)
    rows.append({'Model':name,'Accuracy':accuracy_score(actual,pred),'Precision':precision_score(actual,pred,zero_division=0),'Recall':recall_score(actual,pred,zero_division=0),'F1':f1_score(actual,pred,zero_division=0)})
ml_results=pd.DataFrame(rows); print('\nSTEP 8 — MACHINE LEARNING'); print(ml_results.round(4).to_string(index=False)); ml_results.to_csv(TABLES/f'{STOCK}_08_ml_metrics.csv',index=False)
plt.figure(figsize=(9,4)); plt.bar(ml_results['Model'], ml_results['Accuracy']); plt.ylim(0,1); plt.xticks(rotation=15); plt.title(f'{STOCK} ML Accuracy'); plt.tight_layout(); plt.savefig(CHARTS/f'{STOCK}_06_ml_accuracy.png',dpi=130); plt.close()

# 9 Feature importance
split=int(len(X)*0.8); rf=RandomForestClassifier(n_estimators=150,max_depth=8,min_samples_leaf=5,random_state=42,n_jobs=-1); rf.fit(X.iloc[:split],y.iloc[:split]); imp=pd.Series(rf.feature_importances_,index=fcols).sort_values(ascending=False); imp.rename('Importance').to_csv(TABLES/f'{STOCK}_09_feature_importance.csv')
plt.figure(figsize=(9,4)); imp.head(10).sort_values().plot(kind='barh'); plt.title(f'{STOCK} Top Feature Importance'); plt.tight_layout(); plt.savefig(CHARTS/f'{STOCK}_07_feature_importance.png',dpi=130); plt.close()

# 10 PCA + KMeans
clcols=['Return','Vol20','Mom20','RSI','Volume_Ratio']; cd=data[clcols].dropna().tail(1200); z=StandardScaler().fit_transform(cd); labels=KMeans(n_clusters=4,n_init=10,random_state=42).fit_predict(z); pc=PCA(n_components=2,random_state=42).fit_transform(z)
cluster_summary=pd.DataFrame({'Cluster':labels,'Return':cd['Return'].values,'Volatility':cd['Vol20'].values,'RSI':cd['RSI'].values}).groupby('Cluster').agg(Observations=('Cluster','size'),Mean_Return=('Return','mean'),Mean_Volatility=('Volatility','mean'),Mean_RSI=('RSI','mean')); cluster_summary.to_csv(TABLES/f'{STOCK}_10_kmeans_summary.csv')
plt.figure(figsize=(9,5)); plt.scatter(pc[:,0],pc[:,1],c=labels,s=12); plt.title(f'{STOCK} PCA + KMeans'); plt.xlabel('PC1'); plt.ylabel('PC2'); plt.tight_layout(); plt.savefig(CHARTS/f'{STOCK}_08_pca_kmeans.png',dpi=130); plt.close()

# 11 Anomaly detection
iso=IsolationForest(contamination=0.01,random_state=42); an=iso.fit_predict(z); anomaly_table=pd.DataFrame({'Date':cd.index,'Anomaly':an}); anomaly_table.to_csv(TABLES/f'{STOCK}_11_anomalies.csv',index=False); print('\nSTEP 11 — ANOMALIES:',int((an==-1).sum()))

# 12 Backtesting
bt=data[['Close','Return','MA20','MA50']].dropna().copy(); bt['Signal']=(bt['MA20']>bt['MA50']).astype(int); bt['Strategy_Return']=bt['Signal'].shift(1).fillna(0)*bt['Return']; sr=bt['Strategy_Return']; equity=(1+sr).cumprod(); p=equity.cummax(); sdd=(equity-p)/p; scagr=equity.iloc[-1]**(252/len(equity))-1; svol=sr.std()*np.sqrt(252); ssharpe=sr.mean()/sr.std()*np.sqrt(252); down=sr[sr<0].std(); ssortino=sr.mean()/down*np.sqrt(252) if pd.notna(down) and down!=0 else np.nan; smdd=sdd.min(); calmar=scagr/abs(smdd) if smdd!=0 else np.nan
backtest=pd.DataFrame({'Metric':['Strategy Total Return','Strategy CAGR','Strategy Volatility','Strategy Sharpe','Strategy Sortino','Maximum Drawdown','Calmar Ratio'],'Value':[equity.iloc[-1]-1,scagr,svol,ssharpe,ssortino,smdd,calmar]}); print('\nSTEP 12 — BACKTEST'); print(backtest.round(6).to_string(index=False)); backtest.to_csv(TABLES/f'{STOCK}_12_backtest_metrics.csv',index=False)
plt.figure(figsize=(11,4)); plt.plot(equity.index,equity.values); plt.title(f'{STOCK} Moving Average Strategy Equity Curve'); plt.tight_layout(); plt.savefig(CHARTS/f'{STOCK}_09_backtest_equity_curve.png',dpi=130); plt.close()

# 13 Final summary
best=ml_results.loc[ml_results['Accuracy'].idxmax()]; final=pd.DataFrame({'Stock':[STOCK],'Rows':[len(df)],'Start':[df.index.min().date()],'End':[df.index.max().date()],'Start Price':[df['Close'].iloc[0]],'End Price':[df['Close'].iloc[-1]],'Annualized Volatility':[ret.std()*np.sqrt(252)],'CAGR':[cagr],'Max Drawdown':[dd.min()],'Annualized Sharpe':[ret.mean()/ret.std()*np.sqrt(252)],'Best ML Model':[best['Model']],'Best ML Accuracy':[best['Accuracy']],'Backtest Sharpe':[ssharpe],'Backtest CAGR':[scagr]})
print('\nSTEP 13 — FINAL RESEARCH SUMMARY'); print(final.round(4).to_string(index=False)); final.to_csv(TABLES/f'{STOCK}_13_final_summary.csv',index=False)
print('\nComplete. Charts:',CHARTS); print('Tables:',TABLES)
