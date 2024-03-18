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


# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

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
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# Add Start Button
start_button = Button(text="Start", font=(FONT_NAME, 14, "bold"))
start_button.grid(row=2, column=0)

# Add Checkmark Label
checkmark_label = Label(text="✅", font=(14))
checkmark_label.grid(row=2, column=1)

# Add Reset Button
reset_button = Button(text="Reset", font=(FONT_NAME, 14, "bold"))
reset_button.grid(row=2, column=2)







window.mainloop()