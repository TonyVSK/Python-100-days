from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_in_txtfile():
    ...
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
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
generate_button = Button(text="Generate Password", highlightthickness=0, bg='white')
generate_button.grid(row=3, column=2)

# ADD BUTTON
def activeFunctionFile():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if website and email and password:
        with open("data.txt", "a") as file:
            file.write(f"Website: {website}\nEmail/Username: {email}\nPassword: {password}\n\n")
        website_input.delete(0, END)
        email_input.delete(0, END)
        password_input.delete(0, END)



add_button = Button(text="Add", highlightthickness=0, width=26, bg='white', command=activeFunctionFile)
add_button.grid(row=4, column=1)

# def button_clicked():
#     ...

# # start button
# button1 = Button(text="Start", highlightthickness=0, command = start_counter)
# button1.grid(column=0, row=2)


window.mainloop()