"""
pizza = ["cheese", "pepperoni", "sausage", "banana"]

pizza_answer = input("What is your favorite pizza topping?  ").lower()

for toppings in pizza:
    if answer == toppings:
        print("We have that!")
    if answer != toppings:
        print("We do NOT have that!")
        break
"""
feelings = ["happy", "sad", "angry", "excited", "anxious", "content", "frustrated", "hopeful", "lonely", "curious", "grateful", "bored", "overwhelmed", "inspired", "confused", "relaxed", "nervous", "joyful", "disappointed", "fearful","contento"]

feeling_answer = input("How are you feeling?  ").lower()

if feeling_answer in feelings:
    print("I understand that feeling! =)")
else:
    print("I don't understand that feeling! =(")
    feelings.append(feeling_answer)
