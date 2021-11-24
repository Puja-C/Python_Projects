import random


def guess(x):
    random_number = random.randint(1, x)
    user_guess = 0
    while user_guess != random_number :
        user_guess = int(input("Guess a number: "))
        if user_guess > random_number :
            print("Oops! Too high! Try again.")
        elif user_guess < random_number :
            print("Oops! Too Low! Try again.")
    else :
        print(f"Congratulations! You guessed the number {random_number} correctly!")


guess(15)
