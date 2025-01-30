import random

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(" THIS WEEKS SPANISH QUIZ ")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

whoareyou = input("Are your Mason or Carter? (Mason/Carter)  ").lower()

def carter_spanish_test():
     
    carter_translations = {
        "red haired": "pelirrojo",
        "to be warm": "tener calor",
        "to be cold": "tener frio",
        "to be sleepy": "tener sueno",
        "delicious": "delicioso",
        "to want": "desear",
        "pedir": "to order",
        "main dish": "el plato principal",
        "dessert": "el postre",
        "for dessert": "de postre",
        "rich,tasty": "rico",
        "sugar": "el azucar",
        "spoon": "la cuchara", 
        "knife": "el cuchillo",
        "pepper": "la pimienta",
    
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
        "toothpaste": "la pasta dental",
        "I forgot": "se me olvido",
        "to close": "cerrar",
        "to cash a check": "cobrar un cheque", 
        "to take care of": "cuidar a",
        "dentist": "el dentista",
        "to return": "devolver",
        "gasoline": "la gasolina",
        "to go on foot": "ir a pie",
        "to fill": "llenar",          
        "doctor": "el medico",
        "to take out": "sacar",    
        "opens": "se abre",    
        "closes": "se cierra",    
        "good gracious": "caramba",    
        "almost": "casi",    
        "of course": "como no",    
        "right away": "en sequida",    
        "until": "hasta",    
        "for": "por",    
        "see you soon": "hasta pronto", 
        "to stay": "quedarse",
        "still": "todavia",
        "various": "varios"  
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
