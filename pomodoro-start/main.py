import winsound
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
TIMER = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_fun():
    global REPS
    window.after_cancel(TIMER)
    canvas.itemconfig(canvas_text,text="00:00")
    timer_label.config(text="Timer")
    check_lebel.config(text="")
    REPS = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS
    REPS += 1
    if REPS > 8:
        reset_fun()
    elif REPS % 8 ==0:
        counter(LONG_BREAK_MIN*60)
        timer_label.config(text="Break",fg=RED)
    elif REPS % 2==0:
        counter(SHORT_BREAK_MIN*60)
        timer_label.config(text="Break", fg=PINK)
    else:
        counter(WORK_MIN*60)
        timer_label.config(text="Work", fg=GREEN)
# ---------------------------- POP-UP ON SCREEN ------------------------------- #
def raise_window(window):
    window.attributes('-topmost', 1)
    window.attributes('-topmost', 0)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def counter(count):
    min_count = count // 60
    sec_count = count % 60
    if sec_count < 10:
        sec_count = f"0{sec_count}"

    canvas.itemconfig(canvas_text, text=f"{min_count}:{sec_count}")
    if count > 0:
        global TIMER
        TIMER = window.after(1000, counter, count - 1)
    else:
        raise_window(window)
        marks = ""
        start_timer()
        working_sessions = REPS//2
        for _ in range(working_sessions):
            marks += "✔"
        check_lebel.config(text=marks)
        winsound.Beep(1000, 1000)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
tomato_img = PhotoImage(file="tomato.png")
timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 45, "bold"))
timer_label.grid(row=0, column=1)
button1 = Button(text="Start", bg="white", highlightthickness=0, command=start_timer).grid(row=2, column=0)
button2 = Button(text="Reset", bg="white", highlightthickness=0,command=reset_fun).grid(row=2, column=2)
check_lebel = Label(bg=YELLOW, fg=GREEN)
check_lebel.grid(row=3, column=1)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
canvas_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

window.mainloop()
