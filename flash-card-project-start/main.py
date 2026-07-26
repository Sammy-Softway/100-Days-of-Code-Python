from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    # Try reading the existing progress file
    updated_data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    # Fallback if the user is launching the app for the very first time
    data = pandas.read_csv("data/french_words.csv")
    data_dict = data.to_dict("records")     # CRITICAL CONVERSION: Turns the rows into a list of standalone dictionaries
else:
    data_dict = updated_data.to_dict("records")     # CRITICAL CONVERSION: Turns the rows into a list of standalone dictionaries

current_data = {}

#---------------------------- GENERATE RANDOM WORDS ------------------------------- #

def generate_french_word():
    global current_data, flip_timer

    #Stop the previously scheduled flip_timer execution
    window.after_cancel(flip_timer)

    # Select a random dictionary from our list
    current_data = random.choice(data_dict)
    chosen_french_word = current_data["French"]

    # Update UI to Front/French View
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=chosen_french_word, fill="black")

    canvas.itemconfig(canvas_display_image, image=card_front_img)

    # START A NEW TIMER: Wait 3 seconds, then call show_english_word
    flip_timer = window.after(3000, show_english_word)


def show_english_word():
    # Select the english word from current_data dictionary
    english_word = current_data["English"]

    # Update UI to Back/English View
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=english_word, fill="white")

    canvas.itemconfig(canvas_display_image, image=card_back_img)

def known_word():
    # 1. Remove the dictionary element from our active memory list
    data_dict.remove(current_data)

    # 2. Convert the remaining list back into a Pandas DataFrame
    updated_data = pandas.DataFrame(data_dict)
    # 3. Save it to disk. index=False keeps the data clean without adding raw numbers.
    updated_data.to_csv("data/words_to_learn.csv", index=False)

    # 4. Advance to the next card
    generate_french_word()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flash Card Project")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, show_english_word)

canvas = Canvas(width=800, height=526)
card_back_img = PhotoImage(file="images/card_back.png")
card_front_img = PhotoImage(file="images/card_front.png")

canvas_display_image = canvas.create_image(400, 263, image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

#Texts within canvas
language_text = canvas.create_text(400, 150, text="Language", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))

canvas.grid(column=0, row=0, columnspan=2)


#Buttons
wrong_sign_img = PhotoImage(file="images/wrong.png")
right_sign_img = PhotoImage(file="images/right.png")

wrong_sign_button = Button(image=wrong_sign_img, highlightthickness=0, command=generate_french_word)
wrong_sign_button.grid(column=0, row=1)
right_sign_button = Button(image=right_sign_img, highlightthickness=0, command=known_word)
right_sign_button.grid(column=1, row=1)

generate_french_word()

window.mainloop()