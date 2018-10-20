# CMPT 120 - Lab #6
# YOUR NAME
# DD-MMM-YYYY
###
def showIntro():
        print("Welcome to the Arithmetic Engine!")
        print("=================================\n")
        print("Valid commands are 'add', 'mult', 'sub', 'div', and 'quit'.\n")

def showOutro():
        print("\nThank you for using the Arithmetic Engine…")
        print("\nPlease come back again soon!")
       
def findNums():
        while True:
            try:
                num1 = int(input("Find the first number"))
                num2 = int(input("Find the second number"))
                return(num1, num2)
            except:
                print("Incorrect number")
              
def doLoop():
        while True:
                cmd = input("What computation do you want to perform? ")
                if cmd.lower() == "add":
                    num1, num2 = findNums()
                    result = num1 + num2
                elif cmd.lower() == "sub":
                    num1, num2 = findNums()
                    result = num1 - num2
                elif cmd.lower() == "mult":
                    num1, num2 = findNums()
                    result = num1 * num2
                elif cmd.lower() == "div":
                    num1, num2 = findNums()
                    

                    try:
                        result = num1 // num2
                    except:
                        print("Unable to divide by zero!")
                        continue


                elif cmd.lower() == "quit":
                    break
                else:
                    print("That is an invalid command!")
                    continue
                print("The result is " + str(result) + ".\n")
                
                
def main():
        showIntro()
        doLoop()
        showOutro()
main()
