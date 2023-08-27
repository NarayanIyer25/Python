from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    reset_count_min = '00'
    reset_count_sec = '00'
    canvas.itemconfig(timer_text, text=f"{reset_count_min}:{reset_count_sec}")
    timer_label.config(text = 'Timer', fg=GREEN)
    global  reps
    reps = 0
    tick_label(text='')

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    work_min_sec = WORK_MIN * 60
    short_break_min_sec = SHORT_BREAK_MIN * 60
    long_break_min_sec = LONG_BREAK_MIN * 60

    reps+=1

    if reps% 8 == 0:
        count_down(long_break_min_sec)
        timer_label.config(fg=RED, text="Long Break")
    elif reps %2 == 0:
        timer_label.config(text='Short Break', fg=PINK)
        count_down(short_break_min_sec)

    else:
        timer_label.config(text='Work',fg=GREEN)
        count_down(work_min_sec)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_minutes = math.floor(count/60)
    count_seconds = count % 60

    if count_seconds == 0:
        count_seconds = "00"
    elif count_seconds < 10:
        count_seconds = f'0{count_seconds}'


    canvas.itemconfig(timer_text, text= f"{count_minutes}:{count_seconds}")
    if count> 0 :
        global timer
        timer = window.after(1000,count_down,count-1)
    else:
        start_timer()
        if reps % 2 == 0:
            tick_label['text'] += "✔"
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=110, pady=50 , background=YELLOW)

canvas = Canvas(width=200, height=224, background=YELLOW ,highlightbackground= YELLOW)
img = PhotoImage(file="D:\\PyCharmProjects\\Day28\\tomato.png")
canvas.create_image(103,110,image = img)
timer_text = canvas.create_text(103,110,text="00:00", font=(FONT_NAME,25,'bold') , fill="white")
canvas.grid(row= 1 , column=1)



timer_label = Label(fg=GREEN, font=(FONT_NAME,15,'bold'),bg=YELLOW,text='TIMER')
timer_label.grid(row=0,column=1)




start_button = Button(command=start_timer)
start_button['text'] = "Start"
start_button.grid(row=2,column= 0 )



tick_label = Label(fg=GREEN, font=(FONT_NAME,15,'bold'),bg=YELLOW)
tick_label.grid(row=3,column=1)

reset_button = Button(command=reset_timer)
reset_button['text'] = "Reset"
reset_button.grid(row=2,column= 2, )





window.mainloop()
