import random

def roll_dice():

    dice_image = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │ ",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│    ●    │",
        "│         │",
        "│    ●    │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│ ●       │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│ ●     ● │",
        "│         │",
        "│ ●     ● │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│ ●     ● │",
        "│    ●    │",
        "│ ●     ● │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│ ●     ● │",
        "│ ●     ● │",
        "│ ●     ● │",
        "└─────────┘",
    ),
}
    roll = input("Roll dice?(Yes/No): ")
    while roll.lower() == 'yes':
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        print("Dice rolled: {} and {}".format(dice1, dice2))
        print("\n".join(dice_image[dice1]))
        print("\n".join(dice_image[dice2]))

        roll = input("Roll again?(Yes/No): ")

roll_dice()