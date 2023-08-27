import tkinter

window = tkinter.Tk()
window.minsize(300, 300)


def calculate_miles():
    miles = float(conversion.get())
    km = miles * 1.6
    miles_label.config(text = f"{km}")

miles_label_name = tkinter.Label()
miles_label_name.grid(row=0, column=3)
miles_label_name['text'] = 'miles'
miles_label_name.config(padx=20, pady=20)

miles_calculate = tkinter.Label()
miles_calculate['text'] = 'is equal to'
miles_calculate.grid(row=1, column=1)
miles_calculate.config(padx=20, pady=20)

convert_km = tkinter.Label()
convert_km['text'] = 'km'
convert_km.grid(row=1, column=3)
convert_km.config(padx=20, pady=20)

conversion = tkinter.Entry()
conversion.grid(row=0, column=2)

miles_label = tkinter.Label()
miles_label['text'] = '0'
miles_label.grid(row=1, column=2)
miles_label.config(padx=20, pady=20)

button = tkinter.Button(text='calculate',command=calculate_miles)
button.grid(row=2, column=2)
button.config(padx=20, pady=20)

window.mainloop()
