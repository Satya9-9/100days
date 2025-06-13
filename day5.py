import string
import random


print(" Welcome to the password generator. ")

alphabets = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]
symbols = [chr(i) for i in range(33, 48)] + [chr(i) for i in range(58, 65)] + [chr(i) for i in range(91, 97)] + [chr(i) for i in range(123, 127)]

numbers = [chr(i) for i in range(48,58)]

num_of_letters = int(input("How many letters do you want? "))
num_of_symbols = int(input("How many symbols do you want? "))
num_of_numbers = int(input("How many numbers do you want? "))

password = ""
password_list = []
for i in range(num_of_letters):
    password += random.choice(alphabets)
    password_list.append(random.choice(alphabets))
for i in range(num_of_symbols):
    password += random.choice(symbols)
    password_list.append(random.choice(symbols))
for i in range(num_of_numbers):
    password += random.choice(numbers)
    password_list.append(random.choice(numbers))

random.shuffle(password_list)
print(f"Your password is: {password}")
print(f"Your password list is: {password_list}")

all = alphabets + symbols + numbers

random.shuffle(all)
password_new = ""
for i in range(num_of_symbols + num_of_numbers + num_of_letters):
    password_new += random.choice(all)
print(password_new)



