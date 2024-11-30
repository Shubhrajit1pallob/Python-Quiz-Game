from question_model import Question
from data import question_data
from quiz_brain import QuizzBrain

question_bank = []

for n in question_data:
    question_text = n["question"]
    question_ans = n["correct_answer"]
    new_question = Question(question_text, question_ans)
    question_bank.append(new_question)

quiz = QuizzBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("The qiuz is completed")
print(f"Your final score is {quiz.score}/{quiz.question_no}")



