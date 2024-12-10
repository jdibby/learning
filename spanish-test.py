import random

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(" THIS WEEKS SPANISH QUIZZ ")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

whoareyou = input("Are your Mason or Carter? (Mason/Carter)  ").lower()

def carter_spanish_test():
     
    carter_translations = {
        "person": "la persona",
        "hello": "hola",
        "cat": "el gato",
        "dog": "el perro",
        "he/she likes/loves": "le gusta/le enchanta",
        "to open": "abrir",
        "to celebrate": "celebrar",
        "to decorate": "decorar",
        "decorations": "las decoraciones",
        "to videotape": "hacer un video",
        "to prepare": "preparar",
        "video": "el video",
        "to break": "romper",
        "to take photos": "sacar fotos"
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
        "entrance": "la entrada",
        "bargain": "la ganga",
        "sign": "el letrero",
        "sale": "la liquidaciones", 
        "market": "el mercado",
        "exit": "la salida",
        "light": "claro",
        "solid-colored": "de solo un color",
        "dark": "oscuro",
        "pastel": "pastel",          
        "bright": "vivo",
        "What is it made of": "?De que esta hecho?",    
        "It is made of...": "Esta hecho de",    
        "cotton": "algodon",    
        "leather": "cuero",    
        "wool": "lana",    
        "silk": "seda",    
        "synthetic": "tela sintetica",    
        "high": "alto",    
        "low": "bajo",    
        "cash register": "la caja",    
        "cashier": "el cajero",    
        "check": "el cheque",     
        "traveler's check": "el cheque de viajero",
        "gift certificate": "el cupon de reglado"
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
