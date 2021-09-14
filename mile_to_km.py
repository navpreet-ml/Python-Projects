from tkinter import *


def button_clicked():
    new_text = input.get()
    km = int(new_text) * 1.6
    my_new_label1.config(text=km)

km = 1

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=150)
window.config(padx=5, pady=5)

#Label
my_label = Label(text="Miles", font=("Arial", 12, "bold"))
my_label.grid(column=2, row=0)

#Label
my_new_label = Label(text=f"is equal to", font=("Arial", 12, "bold"))
my_new_label.grid(column=0, row=1)
my_new_label.config(padx=0, pady=0)

#Label
my_new_label1 = Label(text="0", font=("Arial", 12, "bold"))
my_new_label1.grid(column=1, row=1)
my_new_label1.config(padx=0, pady=0)

#Label
my_new_label2 = Label(text="Km", font=("Arial", 12, "bold"))
my_new_label2.grid(column=2, row=1)
my_new_label2.config(padx=0, pady=0)

#Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)


#Entry
input = Entry(width=10)
print(input.get())
input.grid(column=1, row=0)

window.mainloop()