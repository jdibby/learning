feelings = [
    "happy", "sad", "angry", "excited", "anxious", "content", "frustrated", "hopeful", "lonely", "curious", "grateful", "bored", "overwhelmed", "inspired", "confused", "relaxed", "nervous", "joyful", "disappointed", "fearful"]

while True:
    feeling_answer = input("How are you feeling? ").lower()

    if feeling_answer in feelings:
        print("I understand that feeling! =)")
        break
    else:
        print("I don't understand that feeling! =(")
        feelings.append(feeling_answer)
        print(f"The feeling '{feeling_answer}' has been added to database")