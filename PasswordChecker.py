import string

special = string.punctuation
has_lower = 0
has_upper = 0
has_number = 0
has_special = 0

pwd = input("Enter your password: ")
if len(pwd) > 8:
    for i in pwd:
        if i.islower():
            has_lower = 1
        if i.isupper():
            has_upper = 1
        if i.isdigit():
            has_number = 1
        if i in special:
            has_special = 1
        
if has_lower == 1 and has_upper == 1 and has_number == 1 and has_special == 1:
        print("Valid Password")
else:
    print("Invalid Password")