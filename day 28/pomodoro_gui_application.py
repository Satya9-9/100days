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
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer2)
    timer.config(text="Timer")
    check.config(text=" ")
    canvas.itemconfig(timer_text,text="00:00")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps +=1
    print(reps)
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60
    if reps == 8:
        timer.config(text="LONG BREAK",fg=RED)
        count_down(long_break_sec)
    elif reps % 2 != 0:
        timer.config(text="WORK",fg=GREEN)
        count_down(work_sec)

    else:
        timer.config(text="SHORT BREAK",fg=PINK)
        count_down(short_break_sec)



    # count_down(5*60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    print(count)
    count_min =math.floor(count/60)
    count_sec = count%60
    # if count_sec==0:
    #     count_sec ="00"

    if count_sec <10:
        # count_sec = "0" + str(count_sec)
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if(count>0):
        global timer2
        timer2 = window.after(1000,count_down,count-1)
    else:
        start_timer()
        work_sessions = math.floor(reps/2)
        mark = ""
        for _ in range(work_sessions):
            mark+=text
        check.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #

from tkinter import *
window = Tk()
window.title("Pomodoro")
window.config(pady=50,padx=100,bg=YELLOW)

canvas = Canvas(height=224,width=200,bg=YELLOW,highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100,100,image = img)
timer_text = canvas.create_text(100,120,text="00:00", font=(FONT_NAME,30,"bold"),fill="white")
canvas.grid(row=1,column=1)

# count_down(5)


#timer label
timer = Label(text="Timer", font=(FONT_NAME,30,"bold"),fg=GREEN,background=YELLOW)
timer.grid(row=0,column=1)


#start and reset button
start = Button(text="Start",fg="black",background="white",highlightthickness=0,command=start_timer)
reset = Button(text="Reset",fg="black",background="white",highlightthickness=0,command=reset_timer)
start.grid(row=2,column=0)
reset.grid(row=2,column=2)

text = "✓"
#timer label
check = Label(font=(FONT_NAME,25,"bold"),fg=GREEN,background=YELLOW)
check.grid(row=3,column=1)










window.mainloop()
