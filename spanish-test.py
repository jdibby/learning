import random

# ANSI escape codes for colors
GREEN = '\033[32m'          
BRIGHT_RED = '\033[1;31m'    
RESET = '\033[0m'            

print(">>>>>>>>>>>>>>>>>>>>>>>>>")
print(" THIS WEEKS SPANISH QUIZ ")
print(">>>>>>>>>>>>>>>>>>>>>>>>>")

whoareyou = input("Are your Mason or Carter? (Mason/Carter)  ").lower()

def carter_spanish_test():
    carter_translations = {
        "to the right of": " a derecha",
        "to the left of": "a la izquirda",
        "better than": "mejor es que",
        "the best": "la mejor",
        "less": "menos",
        "worse than": "peores que",
        "the worst": "el peor",
        "thing": "la cosa",
        "in my opionon ": "para mi",
        "in your opinion": "para ti",
        "possesion": "la possesion"
     
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

        "to be sure": "estar seguro",
        "narrow": "estrecho",
        "You are making me nervous": "Me estas poniendo nervioso",
        "dangerous": "peligroso", 
        "To take away": "guitar",
        "To be careful": "tener cuidado",
        "already": "ya",
        "approximately": "eproximadamente"
        "How do you go to...?" "como se va",          
        "complicated": "complicado",
        "to cross": "cruzar",    
        "straight": "derecho",    
        "from, since": "desde",    
        "to turn": "doblar",    
        "in the middle of": "en medio de",    
        "as far as, up": "hasta",    
        "to drive": "manejar",    
        "subway": "el metro",    
        "to stop": "parar",    
        "for": "por", 
        "to be located": "quedar",
        "to follow": "seguir",
        "to be in a hurry": "tener prisa"
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
