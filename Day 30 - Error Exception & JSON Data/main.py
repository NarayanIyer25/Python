import json
from tkinter import *
from tkinter import messagebox
import random
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [(random.choice(letters)) for char in range(nr_letters)]
    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    password_list += [random.choice(numbers) for char in range(nr_numbers)]
    random.shuffle(password_list)

    password = "".join(password_list)
    password_textbox.get()
    password_textbox.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    value1 = website_textbox.get()
    value2 = email_textbox.get()
    value3 = password_textbox.get()
    new_data={
        value1: {
            "email": value2,
            "password": value3
        }
    }

    if len(value1) == 0 or len(value2) == 0 or len(value3) == 0:
        messagebox.showerror('oops', "please don't leave any fields empty")

    else:
        try:
            with open("D:\PyCharmProjects\json_data.json", "r") as data_file:
                data = json.load(data_file)
                data.update(new_data)
        except FileNotFoundError:
            with open("D:\PyCharmProjects\json_data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open("D:\PyCharmProjects\json_data.json", "w") as data_file:
                json.dump(data,data_file, indent=4)
        finally:
            password_textbox.delete(0, END)
            website_textbox.delete(0, END)

def find_password():
    value1 = website_textbox.get()
    try:
            with open("D:\PyCharmProjects\json_data.json", "r") as data_file:
                data = json.load(data_file)

            values = data[value1]
    except FileNotFoundError:
            messagebox.showerror(title="Error", message="No details for the Website Found")
    except KeyError:
            messagebox.showerror(title="Error", message="No Data file found")

    else:
            messagebox.showinfo(title=value1 , message= f"Email : {values['email']} \nPassword : {values['password']}")




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()

window.title("Password Generator")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, borderwidth=5)
image = PhotoImage(file="D:\PyCharmProjects\password-manager-start\logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website: ", font=(10, 10))
website_label.grid(row=1, column=0)

website_textbox = Entry(width=20)
website_textbox.grid(row=1, column=1)
website_textbox.focus()


website_button = Button(text="Search",command=find_password)
website_button.grid(row=1,column=2)

email_label = Label(text="Email/Username: ", font=(10, 10))
email_label.grid(row=2, column=0)

email_textbox = Entry(width=30)
email_textbox.insert(0,"dhoni.07@gmailcom")
email_textbox.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password: ", font=(10, 10))
password_label.grid(row=3, column=0)

password_textbox = Entry(width=20)
password_textbox.grid(row=3, column=1)

generate_password = Button(text="Generate", command=gen_pass)
generate_password.grid(row=3, column=2)

add_button = Button(text="add", height=1, width=35, command=save)
add_button.grid(column=1, columnspan=2)

window.mainloop()
