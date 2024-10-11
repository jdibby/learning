import random

translations = { 
    "grandparents": "los abuelos",
    "grandfather": "el abuelo",
    "grandmother": "la abuela"
    "grandparents": "los abuelos"
    "grandparents": "los abuelos"
    "grandparents": "los abuelos"
    "grandparents": "los abuelos"
    }.lower()

def spanish_test():
    right = 0
    wrong = 0

    for english_word, spanish_word in translations.items():
        answer = input(f"What is '{english_word}' in Spanish?  ").lower()
        if answer == spanish_word:
            print("Woooohoooo!")
            print("")
            right += 1
        else:
            print(f"You suck! The answer is '{spanish_word}'.")
            print("")
            wrong += 1

    total_questions = right + wrong
    if total_questions > 0:
        score_percentage = (right / total_questions) * 100
    else:
        score_percentage = 0

    print(f"Your total score: {right} correct, {wrong} incorrect.")
    print(f"Your percentage score: {score_percentage:.2f}%")
    print("")
if __name__ == "__main__":
    spanish_test()
