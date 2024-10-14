### Translations ###
translations = {
    "hello": "hola",
    "grandfather": "el abuelo"          
}

### Makes translations into pairs ###
items = list(translations.items())

for english_word, spanish_word in items:
    answer = input(f"What is '{english_word}' in Spanish?  ").lower()
    if answer == spanish_word:
        print("CORRECT")
    else:
        print(f"INCORRECT '{spanish_word}'.")


"""
items = hello: hola
items = grandfather: el abuelo
items = x: y
items = brother: Mason
"""