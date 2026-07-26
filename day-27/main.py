from tkinter import *

def button_clicked():
    new_text = input.get()
    my_label.configure(text=new_text)
    print("Button clicked")

window = Tk()
window.title("My first GUI program")
window.minsize(500, 300)
window.config(padx=100, pady=200)

#Label
my_label = Label(text="Samuel's label", font=("Arial", 24, "bold"))
#to change the label text later in code
my_label['text'] = 'New Text'
my_label.config(text="New Updated Text")
# my_label.pack()
# my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)
my_label.config(padx=20, pady=20)

#Entry
input = Entry(width=40)
# input.pack()
input.grid(column=3, row=2)

#Button
button = Button(text="Click me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

#New Button
new_button = Button(text="New Button", command=button_clicked)
new_button.grid(column=2, row=0)

window.mainloop()