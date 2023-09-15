##################### Normal Starting Project ######################
import random
import smtplib
import pandas
import datetime
letter = ('letter_1.txt','letter_2.txt','letter_3.txt')
today = (datetime.datetime.now().month,datetime.datetime.now().day)
print(today)
data = pandas.read_csv(r'C:\Users\vrman\Downloads\birthday-wisher-normal-start\birthdays.csv')
birthdays_dict = {(value['month'],value['day']) : value for key,value in data.iterrows()}
if today in birthdays_dict.keys():
    final_letter = random.choice(letter)
    with open(r'C:/Users/vrman/Downloads/birthday-wisher-normal-start/letter_templates/'+final_letter) as f:
        content = f.read()
        message = content.replace('[NAME]', birthdays_dict[today]['name'])
        final_message = message.replace('Angela', birthdays_dict[today]['name'])
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user='shankarnarayanan252525@gmail.com',
                             password='jwdbtubartqjuczm')
            connection.sendmail(from_addr='shankarnarayanan252525@gmail.com',
                                to_addrs='narayan.shankar.2506@gmail.com',
                                msg=f'Subject:Happy Birthday\n\n{final_message}.')

