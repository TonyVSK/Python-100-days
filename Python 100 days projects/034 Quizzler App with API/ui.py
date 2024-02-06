from tkinter import *


THEME_COLOR = "#375362"

class QuizInterdace:
    def __init__(self, quote) -> None:
        self.quote = quote
        
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        

        # WEBSITE DEFINITIONS   
        self.Score_text = Label(text="Score: 0", font=('Arial', 12, 'bold'), bg=THEME_COLOR, fg='white')
        self.Score_text.grid(row=0, column=1)


        # Canvas definitions
        self.canvas = Canvas(width=300, height=250, bg='white', highlightthickness=0)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(150, 125, text=self.quote, width=250, font=("Arial", 20, "italic"), fill=THEME_COLOR)





        # Correct and wrong button
        true_image = PhotoImage(file="images/true.png")
        self.correct_button = Button(image=true_image, highlightthickness=0)
        self.correct_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=false_image, highlightthickness=0)
        self.wrong_button.grid(row=2, column=1)       



        self.window.mainloop()