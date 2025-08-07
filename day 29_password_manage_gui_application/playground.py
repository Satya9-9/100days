# from tkinter import *
# window = Tk()
#
# r = Label(bg= "red", width=20,height=5)
# r.grid(row=0,column=0)
#
# b = Label(bg= "blue", width=20,height=5)
# b.grid(row=1,column=1)
#
# g = Label(bg= "green", width=40,height=5)
# g.grid(row=2,column=0,columnspan=2)
# window.mainloop()



import random
from tkinter import *
from tkinter import messagebox

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

# password_list = []
#
# for char in range(nr_letters):
#   password_list.append(random.choice(letters))
#
# for char in range(nr_symbols):
#   password_list += random.choice(symbols)
#
# for char in range(nr_numbers):
#   password_list += random.choice(numbers)

password_list = [random.choice(letters) for char in range(nr_letters)]
password_list += [random.choice(symbols) for char in range(nr_symbols)]
password_list += [random.choice(numbers) for char in range(nr_numbers)]
random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")