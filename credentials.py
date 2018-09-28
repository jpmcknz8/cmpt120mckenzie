# CMPT 120 Intro to Programming
# Lab #5 – Working with Strings and Functions
# Author: Your Name Here
# Created: YYYY-MM-DD

def findName():
    # get user's first and last names
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    fullname = (first + "." + last)
    fullname.split(".")
    return(fullname)

    # TODO modify this to generate a Marist-style username
def createUsername(name):
    username = (name+ "marist.edu")
    return(username)

    # ask user to create a new password
def findStrength():
    
    password = input("Create a new password: ")
    while len(password) < 8:
        print("Fool of a took! That password is feeble!")
        password = input("Create a new password")
    print("The force is strong in this one...")
    return(password)
    
def goodbye(user):
    print("Account configured. Your new email address is",
    user + "@marist.edu")

def main():
    # Get user's first and last names
    
    # Modify this to generate a Marist-style username
    user = createUsername(findName())
    # Ask user to create a new password
    password = findStrength()
    #Tell user their final info
    info = goodbye(user)
    
main()

