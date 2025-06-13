print("welcome to the tip calculator")

total = float(input("what is your total bill?"))
tip = int(input("how much tip would you like to give? 10, 12, or 15? "))

people = int(input("how many people to split the bill? "))



calc = (total+(tip*total)/100)/people

print(f"Each person should pay: ${round(calc,2)}")
