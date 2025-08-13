import random
from tkinter import *
from tkinter import messagebox
import pyperclip
import json
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

    password_list = [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    password_list += [random.choice(numbers) for char in range(nr_numbers)]
    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0,password)
    pyperclip.copy(password)


    print(f"Your password is: {password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_to_file():
    website_Data = website_input.get().lower().strip()
    email_username_data = mail_username__input.get()
    password_data = password_input.get()

    new_data = {
        website_Data : {
            "email": email_username_data,
            "password":password_data
        }
    }
    if len(password_data) == 0 or len(website_Data) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any field empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                # reading the data inside the data file
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json","w") as data_file:
                #writing to the data file
                json.dump(new_data,data_file,indent=4)

        else:
            print(data)
            #updating the old data with new data
            data.update(new_data)

            with open("data.json","w") as data_file:
                # saving updated data
                json.dump(data,data_file, indent= 4)

        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)
            website_input.focus()



# ---------------------------- Search ------------------------------- #
def find_password():

    website_data = website_input.get().lower()
    try:
        with open("data.json","r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website_data in data:
            email = data[website_data]["email"]
            password = data[website_data]["password"]
            messagebox.showinfo(title=website_data, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website_data} exists.")





# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

# creating canvas
canvas = Canvas(height=200, width=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

# creating website label
website_label = Label(text="Website: ")
website_label.config(padx=5,pady=5)
website_label.grid(row=1, column=0)

# creating E-mail/Username label
mail_username_label = Label(text="E-mail/Username: ")
mail_username_label.config(pady=5,padx=5)
mail_username_label.grid(row=2, column=0)

# creating Password label
password_label = Label(text="Password: ")
password_label.config(padx=5,pady=5)
password_label.grid(row=3, column=0)

# creating entry
website_input = Entry(width=20)
website_input.grid(row=1, column=1)
website_input.focus()

# creating main entry
mail_username__input = Entry(width=40)
mail_username__input.grid(row=2, column=1, columnspan=2)
mail_username__input.insert(0, "satya1729kumar@gmail.com")

# creating password entry
password_input = Entry(width=20)
password_input.grid(row=3, column=1)

# Generate Password Button
generate_password_button = Button(text="Generate Password",command=generate_password)
generate_password_button.grid(row=3, column=2)


# Search Button
search_button = Button(text="Search", width=16,command=find_password)
search_button.grid(row=1, column=2)

# Add Button
add_button = Button(width=35, text="Add", command=add_to_file)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
