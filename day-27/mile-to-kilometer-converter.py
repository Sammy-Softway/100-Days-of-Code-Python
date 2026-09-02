from tkinter import *

def calculate():
    answer = float(miles_entry.get()) * 1.60934
    answer = round(answer)
    converted_label.config(text=f"{answer}")


window = Tk()
window.title("Mile to kilometer Converter")
window.minsize(400, 300)
window.config(padx=100, pady=100)

miles_entry = Entry(width=10, font=("Arial", 20))
miles_entry.grid(row=0, column=1)

equal_label = Label(text="is equal to", font=("Arial", 20))
equal_label.grid(row=1, column=0)

miles_label = Label(text="Miles", font=("Arial", 20))
miles_label.grid(row=0, column=2)
miles_label.config(padx=20, pady=20)

km_label = Label(text="Km", font=("Arial", 20))
km_label.grid(row=1, column=2)
km_label.config(padx=20, pady=20)

converted_label = Label(text="0", font=("Arial", 20))
converted_label.grid(row=1, column=1)

calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(row=2, column=1)


window.mainloop()