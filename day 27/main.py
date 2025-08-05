from tkinter import *

window = Tk()
window.title("My First GUI program")
window.minsize(width=500, height=500)

# Label
my_label = Label(text="i am a label", font=("Times New Roman", 24, "bold"))
# this will keep out label on the screen
# my_label.pack()
# my_label.place(x=100,y=200)
my_label.grid(row=0,column=0)

# multiple ways to change the passed keyword arguments
my_label.config(text="NEW TEXT")


# now we will import new class from tkinter module i.e. is button
# whenever click me button gets clicked command argument will call
# button clicked function that will print i got clicked

def button_clicked():
    txt = input.get()
    print(txt)
    my_label["text"] = txt


button = Button(text="CLICK ME", command=button_clicked)
# button.pack()
button.grid(row=1,column=1)
button.config(padx=40,pady=40)

button2 = Button(text="CLICK ME2", command=button_clicked)
# button.pack()
button2.grid(row=0,column=2)
# now if we want to give any input in our widget then we will call the class
# entry that will take the user input

input = Entry(width=30)
input.insert(END, string="write here text")
# gets text in input
txt = input.get()
print(txt)
# input.pack()
input.grid(row=3,column=3)





window.mainloop()  # thsi will keep window open
