import random
import string

def generate(min_Lenght, numbers=True, specialchar=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    character = letters
    if numbers:
        character += digits
    if specialchar:
        character += special

    pwd = ""
    meet_req = False
    has_number = False
    has_special = False

    while not meet_req or len(pwd) < min_Lenght:
        new_char = random.choice(character)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meet_req = True
        if numbers:
            meet_req = has_number
        if specialchar:
            meet_req = meet_req and has_special 

    return(pwd)

min_lenght = int(input("Enter the minimum lenght: "))
has_number = input("Do you want to include numbers in your password? (y/n): ").lower() == "y" 
has_special = input("Do you want to include special numbers in your password? (y/n): ").lower() == "y"
pwd = generate(min_lenght, has_number, has_special)
print("The generate password is", pwd)
