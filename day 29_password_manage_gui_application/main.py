import random
from tkinter import *
from tkinter import messagebox
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
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

    password = "".join(password_list)
    password_input.insert(0,password)
    pyperclip.copy(password)

    # password = ""
    # for char in password_list:
    #     password += char

    print(f"Your password is: {password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_to_file():
    website_Data = website_input.get()
    email_username_data = mail_username__input.get()
    password_data = password_input.get()
    if len(password_data) == 0 or len(website_Data) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any field empty")
    else:
        print(website_Data, "\n", email_username_data, "\n", password_data)
        is_ok = messagebox.askokcancel(title=website_Data, message=f"These are the details entered: "
                                                                   f"\nEmail: {email_username_data} "
                                                                   f"\nPassword: {password_data}"
                                                                   f"\nIs it OK to save?", )
        if is_ok:
            with open("data.txt", "a") as data:
                data.write(f"{website_Data} || {email_username_data} || {password_data}\n")
                website_input.delete(0, END)

                password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40, bg="white")

# creating canvas
canvas = Canvas(height=200, width=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

# creating website label
website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)

# creating E-mail/Username label
mail_username_label = Label(text="E-mail/Username: ")
mail_username_label.grid(row=2, column=0)

# creating Password label
password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)

# creating entry
website_input = Entry(width=40)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()

# creating main entry
mail_username__input = Entry(width=40)
mail_username__input.grid(row=2, column=1, columnspan=2)
mail_username__input.insert(0, "satya1729kumar@gmail.com")

# creating password entry
password_input = Entry(width=22)
password_input.grid(row=3, column=1)

# Generate Password Button
generate_password_button = Button(text="Generate Password", width=16,command=generate_password)

generate_password_button.grid(row=3, column=2)

# Add Button
add_button = Button(width=35, text="Add", command=add_to_file)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
