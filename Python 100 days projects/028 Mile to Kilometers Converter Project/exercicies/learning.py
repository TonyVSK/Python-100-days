from tkinter import *

# equivalent to screen class in turtle module
window = Tk()
window.title('My First GUI Program')
window.minsize(width=600, height=600)


#Label
my_label = Label(text="I Am a Label", font = ("Arial", 24, "bold"))
my_label.grid(column=0, row=0)
# my_label.pack() # We need it to show the label at the screen in the program



my_label["text"] = "My Tkinter Program"
# it needs to be at the end of the program


def button_clicked():
    # my_label.config(text="Button got clicked")
    new_text = input.get()
    my_label["text"] = new_text
    

# my botton
button = Button(text="Click me", command = button_clicked)
button.grid(column=1, row=1)
# button.pack() # to appear at the screen, this command is necessary


# Entry
input = Entry(width=10)
input.grid(column=0, row=3)



window.mainloop()
