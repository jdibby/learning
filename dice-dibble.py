import random

start_playing = input("Do you want to play a dice game? (y/n").lower()

count = 0

if start_playing == "y" and count < 10000:
    number = random.randint(1,6)
    print("test")

keep_playing = "y"

while keep_playing == "y":
    number = random.randint(1,6)
    if number == 1:
        print("/-------\\")
        print("|       |")
        print("|   0   |")
        print("|       |")
        print("\-------/")
    elif number == 2:
        print("/-------\\")
        print("| 0     |")
        print("|       |")
        print("|     0 |")
        print("\-------/")
    elif number == 3:
        print("/-------\\")
        print("| 0     |")
        print("|   0   |")
        print("|     0 |")
        print("\-------/")
    elif number == 4:
        print("/-------\\")
        print("| 0   0 |")
        print("|       |")
        print("| 0   0 |")
        print("\-------/")
    elif number == 5:
        print("/-------\\")
        print("| 0   0 |")
        print("|   0   |")
        print("| 0   0 |")
        print("\-------/")
    elif number == 6:
        print("/-------\\")
        print("| 0 0 0 |")
        print("|       |")
        print("| 0 0 0 |")
        print("\-------/")
    else:
        break 
    keep_playing = input("press y to roll again and n to exit:")
    print("\n")