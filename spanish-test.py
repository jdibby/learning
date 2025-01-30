import random

# ANSI escape codes for colors
GREEN = '\033[32m'           # Standard green
BRIGHT_RED = '\033[1;31m'    # Brighter red
RESET = '\033[0m'            # Reset to default

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

    correct_count = {word: 0 for word in carter_translations}

    items = list(carter_translations.items())

    while any(count < 2 for count in correct_count.values()):
        random.shuffle(items)
        for english_word, spanish_word in items:
            if correct_count[english_word] >= 2:
                continue

            answer = input(f"What is '{english_word}' in Spanish?  ")
            if answer == spanish_word:
                print(f"{GREEN}CORRECT{RESET}")
                right += 1
                correct_count[english_word] += 1
                if correct_count[english_word] >= 2:
                    print(f"{GREEN}THIS WORD HAS BEEN REMOVED FROM YOUR LIST{RESET}")
            else:
                print(f"{BRIGHT_RED}INCORRECT: '{spanish_word}'{RESET}")
                wrong += 1

    total_questions = right + wrong
    score_percentage = (right / total_questions) * 100 if total_questions > 0 else 0

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
        "right away": "en seguida",    
        "until": "hasta",    
        "for": "por",    
        "see you soon": "hasta pronto", 
        "to stay": "quedarse",
        "still": "todavia",
        "various": "varios"  
    }

    right = 0
    wrong = 0

    correct_count = {word: 0 for word in mason_translations}

    items = list(mason_translations.items())

    while any(count < 2 for count in correct_count.values()):
        random.shuffle(items)
        for english_word, spanish_word in items:
            if correct_count[english_word] >= 2:
                continue

            answer = input(f"What is '{english_word}' in Spanish?  ")
            if answer == spanish_word:
                print(f"{GREEN}CORRECT{RESET}")
                right += 1
                correct_count[english_word] += 1
                if correct_count[english_word] >= 2:
                    print(f"{GREEN}THIS WORD HAS BEEN REMOVED FROM YOUR LIST{RESET}")
            else:
                print(f"{BRIGHT_RED}INCORRECT: '{spanish_word}'{RESET}")
                wrong += 1

    total_questions = right + wrong
    score_percentage = (right / total_questions) * 100 if total_questions > 0 else 0

    print(f"\nYour total score: {right} correct, {wrong} incorrect.")
    print(f"Your percentage score: {score_percentage:.2f}%")
    print("")

if whoareyou == "carter":
    carter_spanish_test()
else:
    mason_spanish_test()
