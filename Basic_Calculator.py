def add(x,y) :
    result = x + y
    print(str(x) + "+" + str(y) + "=" + str(result))


def sub(x, y) :
    result = x - y
    print(str(x) + "-" + str(y) + "=" + str(result))


def mult(x, y) :
    result = x * y
    print(str(x) + "*" + str(y) + "=" + str(result))


def div(x, y) :
    result = x / y
    print(str(x) + "/" + str(y) + "=" + str(result))


while True:

    choice = input("Enter you choice of operation among +, -, *, /, exit : ")
    if choice == '+':
        print("Addition")
        x = input("Enter first number: ")
        y = input("Enter second number: ")
        add(int(x), int(y))
    elif choice == '-' :
        print("Subtraction")
        x = input("Enter first number: ")
        y = input("Enter second number: ")
        sub(int(x), int(y))
    elif choice == '*' :
        print("Multiplication")
        x = input("Enter first number: ")
        y = input("Enter second number: ")
        mult(int(x), int(y))
    elif choice == '/' :
        print("Division")
        x = input("Enter first number: ")
        y = input("Enter second number: ")
        div(int(x), int(y))
    elif choice == 'exit' :
        print("You have decided to exit the program.")
        quit()
    else:
        print("Invalid input. Try Again!")
