from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
question_bank = []
data = question_data
for ques in data:
    question_bank.append(Question(ques['text'], ques['answer']))
quiz_brain = QuizBrain(question_bank)
while quiz_brain.Still_has_questions():
    quiz_brain.next_question()

print("You've completed the quiz")
print(f"Your Final Score was: {quiz_brain.score}/{quiz_brain.question_number}")