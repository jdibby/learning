age = int(input("How old are you? (in number form)  "))
print(type(age))

age = int(age)
print(type(age))



def Rerun():
    try:
        if age > 12 and age < 20:
            print("You are a teenager")
        else:
            print("You are NOT a teenager")
    except ValueError:
        print("you did not type a valid number please try again"   )
        Rerun()
