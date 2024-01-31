from tkinter import *
from tkinter import messagebox
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    password_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for item in range(nr_letters)]
    password_symbols = [random.choice(symbols) for item in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for item in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers




    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def activeFunctionFile():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    is_ok = messagebox.askokcancel(title=website, message=f'These are the details entered: \nEmail: {email}\nPassword: {password}\n\nIs it ok to save?')

    if (is_ok) and (website and email and password):


        with open("data.txt", "a") as file:
            file.write(f"\nWebsite: {website}\nEmail/Username: {email}\nPassword: {password}\n\n")
        website_input.delete(0, END)
        email_input.delete(0, END)
        password_input.delete(0, END)

    else:
        if len(website) == 0 or len(password) ==0:
            messagebox.showinfo(title='Oops', message="Please make sure you haven't left any fields empty")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="white")


# Canvas definitions
canvas = Canvas(width=200, height=200, bg='white', highlightthickness=0)
canvas.grid(row=0, column=1)
# Creating image and text lock logo image
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

# WEBSITE DEFINITIONS
website_text = Label(text="Website:", font=('Arial', 12), bg='white')
website_text.grid(row=1, column=0)
# Entry
website_input = Entry(width=50)
website_input.grid(row =1, column=1, columnspan=2)
website_input.focus()

# EMAIL/USERNAME DEFINITIONS DEFINITIONS
email_text = Label(text="Email/Username:", font=('Arial', 12), bg='white')
email_text.grid(row=2, column=0)
# Entry
email_input = Entry(width=50)
email_input.grid(row=2, column=1, columnspan=3)
email_input.focus()

# PASSWORD DEFINITIONS DEFINITIONS
password_text = Label(text="Password:", font=('Arial', 12), bg='white')
password_text.grid(row=3, column=0)
# Entry
password_input = Entry(width=32)
password_input.grid(row=3, column=1)
password_input.focus()
# Button password
generate_button = Button(text="Generate Password", highlightthickness=0, bg='white', command=generate_password)
generate_button.grid(row=3, column=2)

# ADD BUTTON




add_button = Button(text="Add", highlightthickness=0, width=26, bg='white', command=activeFunctionFile)
add_button.grid(row=4, column=1)

# def button_clicked():
#     ...

# # start button
# button1 = Button(text="Start", highlightthickness=0, command = start_counter)
# button1.grid(column=0, row=2)


window.mainloop()