from tkinter import *
import pandas as pd
import random


data = pd.read_csv("./data/french_words.csv")
to_learn = data.to_dict(orient="records")


def next_card():
    current_card = random.choice(to_learn)
    canvas.itemconfig(word_text2, text=current_card["French"])




# ===================================================================================================
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


# Canvas definitions


# Creating card image
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=front_image)
word_text = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
word_text2 = canvas.create_text(400, 263, text=data["French"][random.randint(0, 99)], font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=next_card)
right_button.grid(row=1, column=1)




next_card()

window.mainloop()