import random

from arts import *
from game_data import *



game_data_dict = data_pro
name = []
follower_cnt = []
description = []
country = []
i = random.randint(0,len(game_data_dict)-1)
j = random.randint(0,len(game_data_dict)-1)
score = 0
for q in range(len(game_data_dict)):
    name.append(game_data_dict[q]['name'])
    follower_cnt.append(game_data_dict[q]['follower_count'])
    description.append(game_data_dict[q]['description'])
    country.append(game_data_dict[q]['country'])

def higher_lower(score, i, j):
    print(logo1)
    if score >0:
        print("You're right! Current score: ", score)


    print(f"\nCompare A: {name[i].title()}, a {description[i]} from {country[i]}")
    print(logo2)
    print(f"Against B: {name[j].title()}, a {description[j]} from {country[j]}\n")

    choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    a = follower_cnt[i]
    b = follower_cnt[j]

    if choice == 'a' and a >= b or choice == 'b' and a <= b:
        i = j
        j = random.randint(0,len(game_data_dict)-1)
        while j == i:
            j = random.randint(0,len(game_data_dict)-1)
        score += 100
        print("you are right")
        print("\n" * 5)
        higher_lower(score, i, j)


    else:
        print("\n" * 10)
        print(logo1)
        print("Sorry, that's wrong. Final score: ", score)

print(logo1)
higher_lower(score, i, j)