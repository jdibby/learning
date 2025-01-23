import random

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(" THIS WEEKS SPANISH QUIZ ")
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
        "bank": "el banco",
        "downtown": "en centro",
        "doctor's/dentist office": "el consultorio",
        "service station": "la estacion de servicio", 
        "pharmacy": "la farmacia",
        "supermarket": "el supermercado",
        "mailbox": "el buzon",
        "letter": "la carta",
        "to mail a letter": "ehar una carta",
        "post office": "el correo",          
        "to send": "enviar",
        "stamp": "el sello",    
        "card": "la tarjeta",    
        "sports equitment": "el equipo deportivo",    
        "golf club": "el palo de golf",    
        "skates": "los patines",    
        "ball": "la pelota",    
        "tennis racket": "la raqueta de tennis",    
        "toothbrush": "el cepillo de dientes",    
        "shampoo": "el champoo",    
        "soap": "el jabon"    
    
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
