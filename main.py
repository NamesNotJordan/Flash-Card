from tkinter import *
from tkinter import messagebox
import pandas
import random

# CONSTANTS
BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")
# --------LOGIC------------------


data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")


def next_card():
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_card["French"])

def flip_card():
    pass
# ----------UI----------------------

app = Tk()
app.title("Flashy")
app.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Card
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")

canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(400, 150, text="Title", font=TITLE_FONT)
card_word = canvas.create_text(400, 263, text="Word", font=WORD_FONT)
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

right_button = Button(image=right_image, highlightthickness=0, command=next_card)
right_button.grid(column=0, row=1)

wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=1, row=1)


# Run App
app.mainloop()
