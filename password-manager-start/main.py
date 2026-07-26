from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

from pandas._libs import join

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_part = [choice(letters) for _ in range(randint(8, 10))]
    symbols_part = [choice(symbols) for _ in range(randint(2, 4))]
    numbers_part =[choice(numbers) for _ in range(randint(2, 4))]

    password_list = letters_part + symbols_part + numbers_part
    shuffle(password_list)
    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email_username = email_username_entry.get()
    password = password_entry.get()

    if website == "" or email_username == "" or password == "":
        messagebox.showinfo("Ooops", "Please enter all required information")
    else:
        correct_details = messagebox.askokcancel(f"{website}", f"These are the details you have entered\n"
                                         f"Email / Username: {email_username}\n"
                                         f"Password: {password}\n Is this correct?\n")

        if correct_details:
            with open("password_manager.txt", "a") as file:
                file.write(f"{website} | {email_username} | {password}\n")

            website_entry.delete(0, "end")
            email_username_entry.delete(0, "end")
            password_entry.delete(0, "end")

            website_entry.focus()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.configure(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

#Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_username_label = Label(text="Email / Username:")
email_username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

#Entries
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_username_entry = Entry(width=35)
email_username_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

#Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()