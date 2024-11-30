class QuizzBrain:
    def __init__(self, question_list):
        self.question_no = 0
        self.question_list = question_list
        self.score = 0

    def still_has_question(self):
        return self.question_no < len(self.question_list)

    def next_question(self):
        # current_question is a question object tha is created.
        current_question = self.question_list[self.question_no]
        self.question_no += 1
        user_answer = input(f"Q {self.question_no}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.ans)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("you got it right!")
            self.score += 1
        else:
            print("That's the wrong answer")
        print(f"The correct answer is {correct_answer}")
        print(f"The current score is {self.score}/{self.question_no}")
        print("\n")
