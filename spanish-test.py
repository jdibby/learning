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
        answer = input(f"What is '{english_word}' in Spanish?  ")
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
        "to participate": "participar",
        "to take lessons": "tomar lecciones",
        "to return": "volver",
        "to create a webpage": "crear una pagina Web", 
        "to be online": "estar en linea",
        "to do a search": "hacer una busqueda",
        "to surf the web": "navegar en la red",
        "to visit chat rooms": "visitar salones de chat",
        "among, between": "entre",
        "interest": "el interes",          
        "opportunity": "la oportunidad",    
        "how long...?": "?cuanto tiempo hace que...?",
        "it has been...": "hace + time + que...",
        "as + adj + as": "tan + adj + como",
        "as much/many + noun + as": "tantos + noun + como"        
    }
    
    right = 0
    wrong = 0

    # Shuffle questions for randomness
    items = list(mason_translations.items())
    random.shuffle(items)

    for english_word, spanish_word in items:
        answer = input(f"What is '{english_word}' in Spanish?  ")
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
