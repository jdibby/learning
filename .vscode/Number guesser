import random

def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False

    print("#############################")
    print("CARTERS NUMBER GUESSING GAME")
    print("#############################")
    print("I've selected a number between 1 and 100. Can you guess it?")

    while not guessed_correctly:
        user_guess = int(input("Enter your guess: "))
        attempts += 1

        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            guessed_correctly = True
            print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")

number_guessing_game()
