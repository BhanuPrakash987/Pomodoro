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
reps=0
timer=None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    heading.config(text='Timer')
    canvas.itemconfig(timer_text,text="00:00")
    check.config(text='✔')
    global reps
    reps=0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    if reps%8==0:
        heading.config(text="Long Break" ,fg=RED)
        count_down(LONG_BREAK_MIN*60)
    elif reps%2==0:
        heading.config(text="Break",fg=PINK)
        count_down(SHORT_BREAK_MIN*60)
    else:
        heading.config(text="Work",fg=GREEN)
        count_down(WORK_MIN*60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min=count//60
    count_sec=count%60
    if count_sec<10:
        count_sec=f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer=window.after(1000,count_down,count-1)
    else:
        start_timer()
        marks=""
        work_sessions=math.floor(reps/2)
        for _ in range(work_sessions):
            marks+='✔'
        check.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato=PhotoImage(file='tomato.png')
canvas.create_image(100,112, image=tomato)
timer_text=canvas.create_text(100,128,fill='white',text="00:00",font=(FONT_NAME,32,"bold"))
canvas.grid(column=1,row=1)

start=Button(text="Start",bg='white',highlightthickness=0,command=start_timer)
start.grid(column=0,row=2)
reset=Button(text="Reset",bg='white',highlightthickness=0,command=reset_timer)
reset.grid(column=2,row=2)

heading=Label(text='Timer',fg=GREEN,font=(FONT_NAME,35,'bold'),bg=YELLOW)
heading.grid(column=1,row=0)
check=Label(fg=GREEN,bg=YELLOW)
check.grid(column=1,row=3)

window.mainloop()