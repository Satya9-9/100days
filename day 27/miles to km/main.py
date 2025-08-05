from tkinter import *
window = Tk()
window.title("Mile to Km Converter")
window.minsize(height=120,width=100)
window.config(padx=10,pady=10)


#entry
input = Entry(width=10)
input.insert(END, string="0")
input.grid(row=0,column=1)


#miles label
Miles = Label(text="Miles", font=("Times New Roman",20,"bold"))
Miles.grid(row=0,column=2)
# Miles.config(padx=10,pady=10)

# is equal to label
equal_to_label = Label(text="equal to label", font=("Times New Roman",20,"bold"))
equal_to_label.grid(row=1,column=0)

# km value label
km_value = Label(text="0", font=("Times New Roman",20,"bold"))
km_value.grid(row=1,column=1)

# km label
km = Label(text="Km", font=("Times New Roman",20,"bold"))
km.grid(row=1,column=2)

# calculate button
def button_clicked():
    miles =float(input.get())
    km = 1.609 * miles
    km = round(km)
    print(km)
    km_value["text"] = km


calculate_button = Button(text="calculate", command=button_clicked)
# button.pack()
calculate_button.grid(row=2,column=1)
calculate_button.config(pady=10,padx=10)


window.mainloop()
