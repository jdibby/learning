import random

translations = {
    "hello": "hola", 
    "house": "casa",
    "brother": "el hermano"
    }

def spanish_test():
    right = 0
    wrong = 0

    for english_word, spanish_word in translations.items():
        answer = input(f"What is '{english_word}' in Spanish?  ").lower()
        if answer == spanish_word:
            print("Woooohoooo!")
            right += 1
        else:
            print(f"You suck! The answer is '{spanish_word}'.")
            wrong += 1

    print("Your total score:", right)

if __name__ == "__main__":
    spanish_test()
