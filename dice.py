import random
import time
import os
from colorama import init, Fore

# Initialize colorama
init(autoreset=True)

def print_dice_faces(dice):
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]

    # Prepare lines for both dice
    lines = [[] for _ in range(5)]

    for number in dice:
        color = random.choice(colors)
        dice_faces = {
            1: [
                " +-------+ ",
                " |       | ",
                " |   0   | ",
                " |       | ",
                " +-------+ "
            ],
            2: [
                " +-------+ ",
                " | 0     | ",
                " |       | ",
                " |     0 | ",
                " +-------+ "
            ],
            3: [
                " +-------+ ",
                " | 0     | ",
                " |   0   | ",
                " |     0 | ",
                " +-------+ "
            ],
            4: [
                " +-------+ ",
                " | 0   0 | ",
                " |       | ",
                " | 0   0 | ",
                " +-------+ "
            ],
            5: [
                " +-------+ ",
                " | 0   0 | ",
                " |   0   | ",
                " | 0   0 | ",
                " +-------+ "
            ],
            6: [
                " +-------+ ",
                " | 0   0 | ",
                " | 0   0 | ",
                " | 0   0 | ",
                " +-------+ "
            ],
        }

        for i, line in enumerate(dice_faces[number]):
            lines[i].append(color + line)

    # Print the combined lines for both dice
    for line in lines:
        print(' '.join(line))

def roll_dice():
    # Simulate rolling the dice with an animation
    dice = []
    for _ in range(2):  # Roll two dice
        for _ in range(10):  # Rapidly change the face 10 times
            number = random.randint(1, 6)
            print_dice_faces([number, number])  # Show the same number for both temporarily
            time.sleep(0.1)  # Short pause for effect
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console

        # Store final roll for both dice
        final_number = random.randint(1, 6)
        dice.append(final_number)

    # Print the final result for both dice
    print(f"---------------YOUR DICE LANDED ON {dice[0]} and {dice[1]}---------------------")
    print_dice_faces(dice)

    # Calculate total
    total = sum(dice)
    print(f"Total: {total}")

    # Check for snake eyes
    if dice[0] == 1 and dice[1] == 1:
        print(Fore.RED + "                   SNAKE EYES!")
        print(Fore.RED + "---------------------------------")

def main():
    keep_playing = input("Do you want to play the dice game? (y/n): ").lower()

    while keep_playing == "y":
        roll_dice()
        keep_playing = input("Do you want to roll again? (y/n): ").lower()

if __name__ == "__main__":
    main()
