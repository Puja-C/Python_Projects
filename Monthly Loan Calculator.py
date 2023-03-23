# take input of Present value, annual interest rate and time, give back the monthly loan payment amount

def interest():
    print("This is a monthly loan payment calculator!!")
    print("")

    p = float(input("Enter the present value: "))
    r = float(input("Enter the annual rate of interest: "))
    t = int(input("Enter the amount of years: "))

    monthly_rate = r/1200
    months = t * 12
    monthly_payment = p * monthly_rate / (1-(1+monthly_rate)**(-months))
    print("The monthly payment for this loan is %d.2f" % monthly_payment)


interest()
