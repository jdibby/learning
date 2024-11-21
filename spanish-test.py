import random

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(" THIS WEEKS SPANISH QUIZ ")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

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
        "cologne": "el agua de colonia",
        "Brush": "el cepillo",
        "belt": "el cinturon",
        "deodorant": "el desodorante", 
        "shower": "la ducha",
        "gel": "el gel",
        "jewelry": "las joyas",
        "lips": "los labios",
        "make-up": "el maquillaje",
        "to take a shower": "ducharse",          
        "to put on": "ponerse",
        "to go to bed": "acostarse",    
        "to shave": "afeitarse",    
        "to fix": "arreglarse",    
        "to take a bath": "banarse",    
        "to brush": "cepillarse",    
        "to cut one's hair": "cortarste el pelo",    
        "to wake up": "despertarse",    
        "to get up": "levantarse",    
        "to wash": "lavarse",    
        "to borrow": "pedir prestado",    
        "to get ready": "prepararse",    
        "to dry": "secarse",    
        "to get dressed": "vestirse",    
        "to paint, polish": "pintarse"       
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
