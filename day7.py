from pyfiglet import Figlet

f = Figlet(font='slant')  # try fonts like 'block', 'bubble', 'banner'
print(f.renderText('CIPHER'))

alphabets = [chr(i) for i in range(97, 123)]

message = input("enter a message: ").lower()
shift = int(input("enter shift: "))
newmessage = ""
newmessage2 = ""
for index, letter in enumerate(message):
    print(index, letter)
    if letter in alphabets:
        newindex = (alphabets.index(letter) + shift) % 26

        newmessage += alphabets[newindex]

    elif letter == " ":
        newmessage += " "

for index, letter2 in enumerate(newmessage):
    print(index, letter2)
    if letter2 in alphabets:
        newindex2 = (alphabets.index(letter2) - shift) % 26 # here negative indexing works


        newmessage2 += alphabets[newindex2]

    elif letter2 == " ":
        newmessage2 += " "

print(newmessage)
print(newmessage2)