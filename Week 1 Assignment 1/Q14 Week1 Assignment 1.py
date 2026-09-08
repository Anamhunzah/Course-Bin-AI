# Question 14: Percentage of Correct Answers. Input total questions and correct answers. Calculate the percentage score.

total_questions = int(input("Enter total questions: "))
correct_answers = int(input("Enter correct answers: "))

if total_questions > 0 and correct_answers <= total_questions: #logical condition AND

    percentage = (correct_answers / total_questions) * 100

    print("Percentage Score:", percentage, "%")

else:
    print("Please enter valid values.")