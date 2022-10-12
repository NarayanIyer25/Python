class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def Still_has_questions(self):
        if self.question_number <= len(self.question_list):
            return True
        else:
            return False


    def Still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        user_answer = input(f"Q.{self.question_number}: {current_question.text}. (True/False)?:")
        self.question_number += 1
        self.check_answer(user_answer , current_question.answer)

    def check_answer(self,user_answer,current_answer):
        if user_answer.lower() == current_answer.lower():
            print("You're Right")
            self.score += 1
        else:
            print("You're Wrong")
        print(f"The correct answer is {current_answer}")
        print(f"The Score is {self.score}/{self.question_number}")
        print()

