import random


def play() :
    user_choice = input("Enter 'r' for rock, 'p' for paper and 's' for scissors: ")
    if user_choice not in ['r', 'p', 's'] :
        return 'Not valid entry! Try again.'
    else :
        computer_choice = random.choice(['r', 'p', 's'])

        if user_choice == computer_choice :
            return 'Tie!'

        if win_rules(user_choice,computer_choice):
            return f'You won! Computer choose {computer_choice}.'

        return f'Computer choose {computer_choice} and won!'


def win_rules(user, system) :
    # r>s, p>r, s>p
    if (user == 'r' and system == 's') or (user == 'p' and system == 'r')\
            or (user == 's' and system == 'p'):
        return True


print(play())
