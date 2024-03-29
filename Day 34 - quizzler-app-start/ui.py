from tkinter import *
THEME_COLOR = "#375362"
from quiz_brain import QuizBrain

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.value = 0
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, background=THEME_COLOR)


        self.score_label = Label(text=f'Score:{self.quiz.score}')
        self.score_label.grid(row=0, column=1, padx=20, pady=20)


        self.canvas = Canvas(width=300, height=250 )
        self.question_text = self.canvas.create_text(150,125,
                                                     width=280,
                                             text = "Some Quote Text",
                                             fill = THEME_COLOR,
                                            font = ('Arial',20,'italic'))
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)



        self.correctImage = PhotoImage(file=r'C:\Users\vrman\Downloads\quizzler-app-start\images\true.png')
        self.correctButton = Button(image=self.correctImage,command=self.true_pressed)
        self.correctButton.grid(row=2, column=0, padx=20, pady=20)

        self.wrongImage = PhotoImage(file=r'C:\Users\vrman\Downloads\quizzler-app-start\images\false.png')
        self.wrongButton = Button(image=self.wrongImage,command=self.False_pressed)
        self.wrongButton.grid(row=2, column=1, padx=20, pady=20)


        self.get_next_question()


        self.window.mainloop()



    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            q_text =self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text = q_text )
        else:
            self.canvas.itemconfig(self.question_text, text = 'You have completed al the questions')
            self.wrongButton.config(state='disabled')
            self.correctButton.config(state='disabled')



    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.get_feedback(is_right)



    def False_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.get_feedback(is_right)


    def get_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg='green')
            self.value +=1
            self.score_label.config(text=f'Score:{self.quiz.score}')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000,self.get_next_question)


