##Number Guessing game
from random import randint

num = randint(1, 100)
is_win = False

def check(guess):
    global is_win 
    if guess < num:
        print("Your number is too small") 
    elif guess > num:
        print("Your number is too big")
    else:
        print("You got the answer!!!") 
        is_win = True
    
print("Welcome to Number Guessing game")

while is_win == False:
    print(num)
    ans = int(input("Please enter a number between 1-100:"))
    check(ans)

