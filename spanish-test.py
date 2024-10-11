import random

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print("5A CAPUTILO WEEK ONE SPANISH QUIZ ")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

translations = {
    "grandparents": "los abuelos",
    "grandfather": "el abuelo",
    "grandmother": "la abuela",
    "brothers": "los hermanos", 
    "sisters": "las hermanas",   
    "brother": "el hermano",
    "sister": "la hermana",
    "stepbrother": "el hermanastro",
    "stepsister": "la hermanastra",
    "sons": "los hijos",          
    "daughters": "las hijas",    
    "parents": "los padres",
    "father": "el padre"          
}

def spanish_test():
    right = 0
    wrong = 0

    # Shuffle questions for randomness
    items = list(translations.items())
    random.shuffle(items)

    for english_word, spanish_word in items:
        answer = input(f"What is '{english_word}' in Spanish?  ").lower()
        if answer == spanish_word:
            print("CORRECT")
            right += 1
        else:
            print(f"INCORRECT '{spanish_word}'.")
            wrong += 1

    total_questions = right + wrong
    if total_questions > 0:
        score_percentage = (right / total_questions) * 100
    else:
        score_percentage = 0

    print(f"\nYour total score: {right} correct, {wrong} incorrect.")
    print(f"Your percentage score: {score_percentage:.2f}%")
    print("")

if __name__ == "__main__":
    spanish_test()