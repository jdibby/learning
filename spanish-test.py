questions = {
    "hello": "hola",
    "house": "casa"
}

def spanish_test():
    score = 0

    for english_word, spanish_word in questions.items():
        answer = input(f"What is '{english_word}' in Spanish? ").lower()
        if answer == spanish_word:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The answer is '{spanish_word}'.")

    print("Your total score:", score)

if __name__ == "__main__":
    spanish_test()
