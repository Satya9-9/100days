import random

stri = "Satya"
letters_list = [letter for letter in stri]
print(letters_list)

names = ["satya", "ajayrajput", "hariom", "chitransh", "krishna"]
upr = [name.upper() for name in names if len(name) > 5]
print(upr)

# dictonary compreshesion

dict = {name: random.randint(1,100) for name in names }
print(dict)

passed_students = {student:marks for (student,marks) in dict.items() if marks >30}
print(passed_students)
import pandas as pd
students_df = pd.DataFrame([dict])
students_df2 = pd.DataFrame(list(dict.items()), columns=["Name", "Marks"])

for (index, row) in students_df2.iterrows():
    print(index,"\n")
    print(row.Name,"\n")
    print(row.Marks,"\n")