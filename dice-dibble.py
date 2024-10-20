import random

start_playing = input("Would you like to play a dice game? (y/n)  ").lower()

def roll_dice():
    count = 0
    number = random.randint(1,6)
    print("\n")
    if number == 1:
        print("/-------\\")
        print("|       |")
        print("|   0   |")
        print("|       |")
        print("\\-------/")
    elif number == 2:
        print("/-------\\")
        print("| 0     |")
        print("|       |")
        print("|     0 |")
        print("\\-------/")
    elif number == 3:
        print("/-------\\")
        print("| 0     |")
        print("|   0   |")
        print("|     0 |")
        print("\\-------/")
    elif number == 4:
        print("/-------\\")
        print("| 0   0 |")
        print("|       |")
        print("| 0   0 |")
        print("\\-------/")
    elif number == 5:
        print("/-------\\")
        print("| 0   0 |")
        print("|   0   |")
        print("| 0   0 |")
        print("\\-------/")
    elif number == 6:
        print("/-------\\")
        print("| 0 0 0 |")
        print("|       |")
        print("| 0 0 0 |")
        print("\\-------/")
    print("\n")
    keep_playing = input("press y to roll again and n to exit:").lower()
    if keep_playing == "y":
        roll_dice()

if start_playing == "y":
    roll_dice()

