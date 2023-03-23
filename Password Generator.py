import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()" + string.ascii_letters.lower())


def password_generator():
    length = int(input("Enter the desired length of the password: "))

    random.shuffle(characters)
    password = []

    for x in range(length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)

    print("Password is %s." % password)


options = input("Do you want to generate a password: (Yes/No) ")
if options == 'Yes': password_generator()
elif options == 'No':
    print("Program ended!")
    quit()
else:
    print("Invalid input. Please input Yes or No.")
    quit()
