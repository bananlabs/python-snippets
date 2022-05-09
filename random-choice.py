# Game Logic
# Give a list of names inputs separated by comma and space
# Ex: anny, mary, tina, doug, mark
# Choose a name from the list at random to pay the bill
# by @bananlabs

import random 
peoples_name = input("Give me everybody's names, separated by a comma. ")
names = peoples_name.split(", ")

length_list = len(names)

names_choice = random.randint(0, length_list - 1)
print(f"{names[names_choice]} is going to buy the meal today!")