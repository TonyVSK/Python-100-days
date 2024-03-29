from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
CHECK_MARK = "✓"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    #timer_text 00:
    canvas.itemconfig(timer_number, text="00:00")
    # title_label "Timer"
    timer_text.config(text="Timer", fg=GREEN)
    #reset check_marks
    check_marks.config(text = "")

    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_counter():
    global reps
    global timer_number
    reps += 1
    

    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60    

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_text.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_text.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_text.config(text="Work", fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(counter):
    global reps
    global timer

    counter_min = math.floor(counter/60)
    counter_sec = counter%60
    if counter_sec < 10:
        counter_sec = f"0{counter_sec}"
    if counter_min < 10:
        counter_min = f"0{counter_min}"
    canvas.itemconfig(timer_number, text=f'{counter_min}:{counter_sec}')
    # canvas.itemconfig(timer_number, text=f'{counter_min}:{counter_sec}')
    if counter > 0:
        timer = window.after(1000, count_down, counter-1)
    else:
        start_counter()
        mark = ""
        work_sessions = math.floor(reps/2)
        for i in range(0, work_sessions):
            mark += f"{CHECK_MARK}"

        check_marks.config(text = mark)
# ---------------------------- UI SETUP ------------------------------- #
reps = 0
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


# Canvas definitions
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.grid(row=0, column=1)
# Creating image and text POMODORO TOMATO AND SCREEN
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_number = canvas.create_text(100, 130, text = "00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# Timer Text
timer_text = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"), bg=YELLOW)
timer_text.grid(row=0, column=1)

# Start and Reset buttons
def button_clicked():
    ...

# start button
button1 = Button(text="Start", highlightthickness=0, command = start_counter)
button1.grid(column=0, row=2)

# reset button
button2 = Button(text="Reset", highlightthickness=0, command = reset_timer)
button2.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()