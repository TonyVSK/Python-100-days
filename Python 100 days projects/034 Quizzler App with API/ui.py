from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterdace:
    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain
        self.score = 0
        
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        

        # WEBSITE DEFINITIONS   
        self.Score_text = Label(text=f"Score: {self.score}", font=('Arial', 12, 'bold'), bg=THEME_COLOR, fg='white')
        self.Score_text.grid(row=0, column=1)


        # Canvas definitions
        self.canvas = Canvas(width=300, height=250, bg='white', highlightthickness=0)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(150, 125, text="", width=200, font=("Arial", 20, "italic"), fill=THEME_COLOR)





        # Correct and wrong button
        true_image = PhotoImage(file="images/true.png")
        self.correct_button = Button(image=true_image, highlightthickness=0, command=self.check_answer_True)
        self.correct_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=false_image, highlightthickness=0, command=self.check_answer_False)
        self.wrong_button.grid(row=2, column=1)       


        self.get_next_question()




        self.window.mainloop()



    
    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    

    def check_answer_True(self):
        answer = "True"    
        self.result = self.quiz.check_answer(answer)
        if self.result == 1:
            self.score+=1
            Label.config(self.Score_text, text=f"Score: {self.score}")
        try:
            self.get_next_question()
        except IndexError:
            Label.config(self.Score_text, text=f"You finished! you did {self.score} points")
        else:
            pass
    def check_answer_False(self):
        answer = "False"    
        self.result = self.quiz.check_answer(answer)
        if self.result == 1:
            self.score+=1
            Label.config(self.Score_text, text=f"Score: {self.score}")
        try:
            self.get_next_question()
        except IndexError:
            Label.config(self.Score_text, text=f"You finished! you did {self.score} points")
        else:
            pass