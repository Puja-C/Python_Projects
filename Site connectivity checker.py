# give a URL and it will give a response if the site is up and running
# if running--> response 200

import urllib.request as urllib


def main(url) :
    print("Checking connectivity.")

    response = urllib.urlopen(url)
    print("Connected to " + url + " successfully.")
    print("The response code is:", response.getcode())


print("This is a site connectivity checker program.")
url = input("Input the URL of the site: ")

main(url)
