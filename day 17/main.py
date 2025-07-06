from turtle import Turtle, Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# my_screen = Screen()
# print(my_screen.canvheight)
# timmy.forward(100)
# timmy.color("red")
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["pikachu", "squirtle",
                                  "charmender"],align="l")
table.add_column("Type", ["electric","water","fire"],align="l")
print(table)

class User:
    def __init__(self, user_id, user_name):
        print("new user begin created")
        self.user_id = user_id
        self.user_name = user_name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user1 = User("1", "satya")
user2 = User("2", "dhalu")

user1.follow(user2)

print(user1.followers)
print(user2.followers)


print(user2.following)
print(user1.following)
