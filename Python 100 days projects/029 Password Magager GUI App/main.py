from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)


# Canvas definitions
canvas = Canvas(width=200, height=200)
canvas.grid(row=0, column=1)
# Creating image and text POMODORO TOMATO AND SCREEN
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 112, image=logo_image)
canvas.grid(row=1, column=1)




window.mainloop()