# ---------------------------- IMPORT MODULES ------------------------------- #
from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
# ---------------------------- READING DATA WITH PANDAS ------------------------------- #
data = pandas.read_csv("data/french_words.csv")
# --------------------- To get all the words/translation rows out as a list of dictionaries  ------------------- #
word_dictionary = data.to_dict(orient="records")
# ---------------------------- WORD GENERATOR ------------------------------- #


def word_generator():
    random_word = choice(word_dictionary)
    french_word = random_word["French"]
    canvas.itemconfig(title, text="French")
    canvas.itemconfig(word, text=french_word)


# ---------------------------- GUI ------------------------------- #
window = Tk()
window.title("FlashCard App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# ----------------------------CANVAS ------------------------------- #
canvas = Canvas(width=800, height=526)
card_image = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_image)
canvas.config(bg=BACKGROUND_COLOR,  highlightthickness=0)
title = canvas.create_text(400, 150, text="French", font=("Aerial", 40, "italic"))
word = canvas.create_text(400, 263, text="Word", font=("Aerial", 40, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# ----------------------------WRONG BUTTON ------------------------------- #
wrong_image = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong_image,  highlightthickness=0, command=word_generator)
wrong_btn.grid(row=1, column=0)

# ---------------------------- RIGHT BUTTON ------------------------------- #
right_image = PhotoImage(file="images/right.png")
wrong_btn = Button(image=right_image,  highlightthickness=0, command=word_generator)
wrong_btn.grid(row=1, column=1)

word_generator()

window.mainloop()
