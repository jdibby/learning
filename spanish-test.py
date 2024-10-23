import random

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(" THIS WEEKS SPANISH QUIZ ")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")


whoareyou = input("Are your Mason or Carter? (Mason/Carter)  ").lower()

def carter_spanish_test():
     
    carter_translations = {
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
    
    right = 0
    wrong = 0

    # Shuffle questions for randomness
    items = list(carter_translations.items())
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
    
def mason_spanish_test():
     
    mason_translations = {
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
    
    right = 0
    wrong = 0

    # Shuffle questions for randomness
    items = list(mason_translations.items())
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

if whoareyou == "carter":
    carter_spanish_test()
else:
    mason_spanish_test()
