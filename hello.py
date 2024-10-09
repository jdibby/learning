import time
import os

print("Hello world")
Hi = "Hello world!"

print("Hello there")

Name = input("What is your name?   ")

Feeling = input(f"how are you {Name}?   ")
#answer to why needs comment on direct awnser

if Feeling == "Good":
    print(f"Thats good to hear {Name}")
    
    why = input(f"So why are you {Feeling} {Name}?")
    time.sleep(5)
    quit

os.system('clear')
