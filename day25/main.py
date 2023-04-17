import turtle
import pandas
correct_answer=[]
data = pandas.read_csv('50_states.csv')
screen = turtle.Screen()
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
game_is_on = True
score = 0
count = 0
while game_is_on:
    guess_answer = screen.textinput(title=f'{score}/50 State Correct', prompt='What is the State')
    guess_answer.title()
    for i in data.values:
        i[0] = i[0].lower()
        if i[0] == guess_answer and guess_answer not in correct_answer:
            t=turtle.Turtle()
            t.hideturtle()
            t.penup()
            t.setx(i[1])
            t.sety(i[2])
            t.write(guess_answer)
            correct_answer.append(i[0])
            score+=1
    count+=1
    print(count)
    if count == 50:
        game_is_on = False

    if guess_answer == 'exit':
        break

missed_answers = [i[0].lower() for i in data.values if i[0].lower() not in correct_answer]


print(missed_answers)
print(len(missed_answers))
data = pandas.DataFrame(missed_answers)
data.to_csv('missed_answers.csv')




screen.exitonclick()
