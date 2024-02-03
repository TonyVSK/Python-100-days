from tkinter import *
import pandas as pd
import random

try:
    data = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("./data/french_words.csv")
else:
    pass
to_learn = data.to_dict(orient="records")
current_card = {}
# ===================================================================================================
# Functions beeing used
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(word_text, text="French", fill="black")
    canvas.itemconfig(word_text2, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=front_image)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    global current_card
    canvas.itemconfig(word_text, text="English", fill="white")
    canvas.itemconfig(word_text2, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image = card_back_img)


def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()
# ===================================================================================================
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


flip_timer = window.after(3000, flip_card) # after 3 seconds, it will trigger the flip_card function

# Canvas definitions


# Creating card image
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(400, 263, image=front_image)
word_text = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
word_text2 = canvas.create_text(400, 263, text=data["French"][random.randint(0, 99)], font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)




next_card()

window.mainloop()