# file = open("my_txt.txt")

with open("my_txt.txt") as file:
    contents = file.read()
    print(contents)

# file.close() using "with" keyword we don't have any
# problem this file open or closes thats it

with open("my_txt.txt", mode="a") as file:
    file.write("\nsatya")

with open("new_file.md", mode="w") as file:
    file.write("hello")

