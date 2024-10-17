import random

choices = ["rock", "paper", "scissors", "bomb"]

players = input("1 or 2 Player:  ")

def play_the_game_1player():
    if user_choice == computer_choice:
        print("tie")
    elif (user_choice == "rock" and computer_choice == "scissors"):
        print("you win")
    elif (user_choice == "rock" and computer_choice == "paper"):
        print("you lose")
    elif (user_choice == "paper" and computer_choice == "scissors"):
        print("you lose")
    elif (user_choice == "paper" and computer_choice == "rock"):
        print("you win")
    elif (user_choice == "scissors" and computer_choice == "rock"):
        print("you lose")
    elif (user_choice == "scissors" and computer_choice == "paper"):
        print("you win")
    elif (user_choice == "bomb"):
        print("You blew up the AI, you win")
    elif (computer_choice == "bomb"):
        print("AI blew itself up, you win")
    elif (user_choice == "bomb" and computer_choice == "bomb")
        print("you and the AI blew eachother up")
    else:
        print("incorrect response")

def play_the_game_2player():
    if player1_choice == player2_choice:
        print("tie")
    elif (player1_choice == "rock" and player2_choice == "scissors"):
        print("Player 1 Wins")
    elif (player1_choice == "rock" and player2_choice == "paper"):
        print("Player 2 Wins")
    elif (player1_choice == "paper" and player2_choice == "scissors"):
        print("Player 2 Wins")
    elif (player1_choice == "paper" and player2_choice == "rock"):
        print("Player 1 Wins")
    elif (player1_choice == "scissors" and player2_choice == "rock"):
        print("Player 2 Wins")
    elif (player1_choice == "scissors" and player2_choice == "paper"):
        print("Player 1 Wins")
    elif (player1_choice == "bomb" and player2_choice == "bomb"):
        print("Player 1 and Player 2 blew up each other!  You both lose!")
    elif (player1_choice == "bomb"):
        print("Player 1 blew up Player 2, Player 1 Wins")
    elif (player2_choice == "bomb"):
        print("Player 2 blew up Player 1, Player 2 Wins")

    else:
        print("incorrect response")

if players == "1":
    computer_choice = random.choice(choices)
    user_choice = input("Choose Option (rock/paper/scissors)  ").lower()
    if user_choice in choices:
        print(f"You Chose {user_choice} and the AI chose {computer_choice}")
        play_the_game_1player()
elif players == "2":
    player1_choice = input("Player 1:  Choose Option (rock/paper/scissors)  ").lower()
    player2_choice = input("Player 2:  Choose Option (rock/paper/scissors)  ").lower()
    if player1_choice in choices and player2_choice in choices:
        print(f"Player 1 chose {player1_choice} and Player 2 chose {player2_choice}")
        play_the_game_2player()


