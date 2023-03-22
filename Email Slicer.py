# basically this will slice the user input email at @ into a user name and domain
# further it will slice the domain at . into domain and extensions
# tempemail@gmail.com --> tempemail, gmail, com

def main():
    print("Welcome to email slicer!!")
    print("")

    email_id = input("Enter the email id you want to slice:")

    user_name, domain = email_id.split('@')
    domain, extension = domain.split('.')

    print("Username is %s, domain is %s and extension is %s." %(user_name,domain,extension))

main()