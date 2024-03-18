from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    count_down(1 * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_minutes = math.floor(count / 60)
    count_seconds = count % 60

    # If lower than 0 add extra 0
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"
    if count_minutes == 0:
        count_minutes = "00"

    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")
    if count > 0:
        window.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Taha Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Add Timer Label
timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 45, "bold"))
timer_label.grid(row=0, column=1)

# Add Image using Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# Add Start Button
start_button = Button(text="Start", font=(FONT_NAME, 14, "bold"), highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

# Add Reset Button
reset_button = Button(text="Reset", font=(FONT_NAME, 14, "bold"), highlightthickness=0)
reset_button.grid(row=2, column=2)

# Add Checkmark Label
checkmark_label = Label(text="✅", fg=GREEN, bg=YELLOW, font=(14))
checkmark_label.grid(row=3, column=1)

window.mainloop()
