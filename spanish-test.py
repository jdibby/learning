translations = {"hello": "hola", "house": "casa"}

def spanish_test():
    score = 0

    for english_word, spanish_word in translations.items():
        answer = input(f"What is '{english_word}' in Spanish?  ").lower()
        if answer == spanish_word:
            print("Woooohoooo!")
            score += 1
            print(score)
        else:
            print(f"You suck! The answer is '{spanish_word}'.")
            print(score)

    print("Your total score:", score)

if __name__ == "__main__":
    spanish_test()
