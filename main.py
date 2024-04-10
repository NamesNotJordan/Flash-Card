from tkinter import *
import pandas
import random
import time

# CONSTANTS
BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")

current_card = {}
# --------LOGIC------------------

try :
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")

to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    app.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_bg, image=CARD_FRONT_IMAGE)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    flip_timer = app.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(card_bg, image=CARD_BACK_IMAGE)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


def word_has_been_learned():
    to_learn.remove(current_card)
    new_data = pandas.DataFrame(to_learn)
    new_data.to_csv("data/words_to_learn.csv")
    next_card()
# ----------UI----------------------


app = Tk()
app.title("Flashy")
app.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = app.after(3000, func=flip_card)

# Card
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
CARD_FRONT_IMAGE = PhotoImage(file="images/card_front.png")
CARD_BACK_IMAGE = PhotoImage(file="images/card_back.png")
card_bg = canvas.create_image(400, 263, image=CARD_FRONT_IMAGE)
card_title = canvas.create_text(400, 150, text="Title", font=TITLE_FONT)
card_word = canvas.create_text(400, 263, text="Word", font=WORD_FONT)
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
RIGHT_IMAGE = PhotoImage(file="images/right.png")
WRONG_IMAGE = PhotoImage(file="images/wrong.png")
right_button = Button(image=RIGHT_IMAGE, highlightthickness=0, command=word_has_been_learned)
right_button.grid(column=0, row=1)

wrong_button = Button(image=WRONG_IMAGE, highlightthickness=0, command=next_card)
wrong_button.grid(column=1, row=1)


# Run App
next_card()
app.mainloop()
