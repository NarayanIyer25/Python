import time

BACKGROUND_COLOR = "#B1DDC6"
import pandas
from tkinter import  *
import random
try:
    new_Data = pandas.read_csv(r'D:\PyCharmProjects\flash-card-project-start\data\words_to_learn.csv')
except FileNotFoundError:
    data_frame = pandas.read_csv(r'D:\PyCharmProjects\flash-card-project-start\data\french_words.csv')
    data = data_frame.to_dict(orient='records')
else:
    data = new_Data.to_dict(orient='records')


value = {}

def Generate_word():
    global value,flip_timer
    window.after_cancel(flip_timer)
    value =  random.choice(data)
    canvas.itemconfig(title,text='French',fill='black')
    canvas.itemconfig(French_word,text = value['French'],fill='black')
    canvas.itemconfig(card_background,image=front_img)
    flip_timer = window.after(3000, func=Flip_card)


def Flip_card():
    canvas.itemconfig(French_word,text = value['English'],fill='white')
    canvas.itemconfig(title,text = 'English',fill='white')
    canvas.itemconfig(card_background, image=back_img)


def is_known():

    data.remove(value)
    new_data = pandas.DataFrame(data)
    new_data.to_csv(r'D:\PyCharmProjects\flash-card-project-start\data\words_to_learn.csv',index=False)
    Generate_word()



def Flip_card():

    canvas.itemconfig(French_word,text = value['English'],fill='white')
    canvas.itemconfig(title,text = 'English',fill='white')
    canvas.itemconfig(card_background, image=back_img)

window = Tk()
window.title("Flashly")
window.config(padx=20,pady=20,background=BACKGROUND_COLOR)

flip_timer=window.after(1000,func=Flip_card)

canvas = Canvas(width=800,height=526)
front_img = PhotoImage(file=r'D:\PyCharmProjects\flash-card-project-start\images\card_front.png')
back_img = PhotoImage(file=r'D:\PyCharmProjects\flash-card-project-start\images\card_back.png')
card_background = canvas.create_image(400,263,image = front_img)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2,padx=20,pady=20)


right_image = PhotoImage(file=r'D:\PyCharmProjects\flash-card-project-start\images\right.png')
right_button = Button(image=right_image,highlightthickness=0,command=is_known)
right_button.grid(row=1,column=0,padx=20,pady=20)

wrong_image = PhotoImage(file=r'D:\PyCharmProjects\flash-card-project-start\images\wrong.png')
wrong_button = Button(image=wrong_image,highlightthickness=0,command=Generate_word)
wrong_button.grid(row=1,column=1,padx=20,pady=20)

title = canvas.create_text(200,150,text='French',font=('arial',40,'bold'))
French_word = canvas.create_text(200,250,text='French',font=('arial',20,'italic'))

Generate_word()

window.mainloop()