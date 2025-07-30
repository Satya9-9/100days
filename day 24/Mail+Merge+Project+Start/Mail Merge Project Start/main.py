#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("./input/Names/invited_names.txt",mode="r") as names:
    all_names = names.readlines()


with open("./input/Letters/starting_letter.txt", mode="r") as letter:
    letter_content = letter.read()

for name in all_names:
    name = name.strip()
    new_letter = letter_content.replace("[name]", name)
    print(new_letter)

    with open(f"./Output/ReadyToSend/letter_to_{name}.txt" ,mode = "w") as letters:
        letters.write(new_letter)







