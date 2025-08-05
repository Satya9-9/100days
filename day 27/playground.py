
# *args is the way in which we can take
# any number of arguments inside the function
def add(*args):
    # all the arguments gets stored inside the
    # tuple
    print(type(args))
    total = 0
    for n in args:
        total+=n

    return total

print(add(1,2,3,4,5,6,7,8,9,10))

def calculate(n,**kwargs):
    print(type(kwargs))

    for key, value in kwargs.items():
        print(key)
        print(value)

    n +=kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(5,add=2, multiply= 3)

class Car:
    def __init__(self,**kw):
        self.model = kw.get("model")
        self.make = kw.get("make")
        self.color = kw.get("color")
        self.seats = kw.get("seats")

mycar = Car(model= "Nissan",seats=4)
print(mycar.model,mycar.seats,mycar.color)

from tkinter import *

window = Tk()
window.title("My First GUI program")
window.minsize(width=500, height=500)

# Label
my_label = Label(text="i am a label", font=("Times New Roman", 24, "bold"))
# this will keep out label on the screen
my_label.pack()
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
button.pack()

# now if we want to give any input in our widget then we will call the class
# entry that will take the user input

input = Entry(width=30)
input.insert(END, string="write here text")
# gets text in input
txt = input.get()
print(txt)
input.pack()

# text
# this will allow to put some large bunch of text or paragraph

text = Text(height=5, width=30)
# this puts cursor in text box
text.focus()
text.insert(END, chars="Exanple of multiline text-entry")
# get's current value in textbox at line 1, character0
print(text.get("1.0", END))
text.pack()


# spinbox

def spinbox_used():
    # gets the current value in the spinbox.

    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=7, command=spinbox_used)
spinbox.pack()


# Scale
# called with current scale value
def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# checkbutton

def checkbutton_used():
    # this will print state of checkbutton
    # clicked or not clicked
    print(check_state.get())


# variable to hold on to checked state, 0 is off, 1 is on.
check_state = IntVar()
checkbutton = Checkbutton(text="Is ON?", variable=check_state,
                          command=checkbutton_used)
check_state.get()
checkbutton.pack()


# Radiobutton
def radiobutton_used():
    # this will print state of which radiobutton
    # clicked or not clicked
    print(radio_state.get())


radio_state = IntVar()
radiobutto1 = Radiobutton(text="Option1", variable=radio_state,
                          value=1, command=radiobutton_used)
radiobutto2 = Radiobutton(text="Option2", variable=radio_state,
                          value=2, command=radiobutton_used)

radiobutto1.pack()
radiobutto2.pack()


# listbox
def listbox_used(event):
    # this will print current selection from listbox
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=5)
fruits = ["Apple", "Pear", "orange", "mango", "banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)

listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()  # thsi will keep window open
