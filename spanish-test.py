import random

print(">>>>>>>>>>>>>>>>>>>>>>>>>")
print(" THIS WEEKS SPANISH QUIZ ")
print(">>>>>>>>>>>>>>>>>>>>>>>>>")

whoareyou = input("Are your Mason or Carter? (Mason/Carter)  ").lower()

def carter_spanish_test():
     
    carter_translations = {
        "plate": "el plato",
        "salt": "la sal",
        "napkin": "la servilleta",
        "cup": "la taza",
        "fork": "el tenedor",
        "glass": "el vaso",
        "waiter": "el camarero",
        "bill": "la cuenta",
        "menu": "el menu",
        "i need": "me falta",
        "i would like": "quisiera",
        "i will bring you": "le traigo", 
        "will you bring me": "me trae", 
        "i bring": "yo traigo", 
        "now": "ahora",   
        "anything else": "algo mas",   
        "your welcome": "de nada"
    }

    right = 0
    wrong = 0

    # Keep track of how many times each word is answered correctly
    correct_count = {word: 0 for word in carter_translations}

    # Shuffle the questions to randomize
    items = list(carter_translations.items())

# Loop until all words are answered correctly twice
    while any(count < 2 for count in correct_count.values()):
        random.shuffle(items)  # Shuffle questions for randomness
        for english_word, spanish_word in items:
            if correct_count[english_word] >= 2:
                continue  # Skip the word if it's been answered correctly twice
            answer = input(f"What is '{english_word}' in Spanish?  ")
            if answer == spanish_word:
                print("CORRECT")
                right += 1
                correct_count[english_word] += 1
                if correct_count[english_word] >= 2:
                    print("THIS WORD HAS BEEN REMOVED FROM YOUR LIST")
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
        "avenue": "la avenida",
        "truck": "el camion",
        "highway": "cerla carretera",
        "driver": "el conductor", 
        "intersection": "el cruce de calles",
        "block": "la cuadra",
        "corner": "la esquina",
        "statue": "la estatua",
        "fountain": "la fuente",
        "pedestrian": "el peaton",          
        "drivers license": "el permiso de manejar",
        "plaza": "la plaza",    
        "police officer": "el policia",    
        "to give a ticket": "poner una multa",    
        "bridge": "el puente",    
        "stoplight": "el semaforo",    
        "stop sign": "la senal de parada",    
        "traffic": "el trafico",    
        "wide": "anche",    
        "enough": "basta",    
        "OK agreed": "de acuerdo", 
        "To leave": "dejar",
        "leave me alone": "dejame en paz",
        "slowly": "despacio", 
    }   "to wait": "esperar"
    
    right = 0
    wrong = 0

    # Keep track of how many times each word is answered correctly
    correct_count = {word: 0 for word in mason_translations}

    # Shuffle the questions to randomize
    items = list(mason_translations.items())

    # Loop until all words are answered correctly twice
    while any(count < 2 for count in correct_count.values()):
        random.shuffle(items)  # Shuffle questions for randomness
        for english_word, spanish_word in items:
            if correct_count[english_word] >= 2:
                continue  # Skip the word if it's been answered correctly twice

            answer = input(f"What is '{english_word}' in Spanish?  ")
            if answer == spanish_word:
                print("CORRECT")
                right += 1
                correct_count[english_word] += 1  # Increment correct count for this word
                if correct_count[english_word] >= 2:
                    print("THIS WORD HAS BEEN REMOVED FROM YOUR LIST")
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
