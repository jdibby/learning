
age = input("What is your age?  ")

if age:
    try:
        newage = int(age)
        print("Your age is", newage)
    except:
        print("Not a valid age")


### TEST