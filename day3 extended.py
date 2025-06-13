print(" Welcome to Treasure Island.Your mission is to find the treasure.")
ans = input("left or right? ").lower()
if ans == "left":
    s_ans = input("swim or wait? ").lower()
    if s_ans == "wait":
        t_ans = input("Which door? RED, BLUE, YEllOW or ANYTHING ELSE ").lower()
        if t_ans == "red":
            print("burned by fire Game Over")

        elif t_ans == "blue":
            print(" Eaten by breasts Game Over")

        elif t_ans == "yellow":
            print(" You Win! ")

        else:
            print(" Game Over ")
    else:
        print(" Attacked by trout Game Over")

else:
    print("Fall into a hole")
