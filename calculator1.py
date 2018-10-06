# Calculator.py
def getPieces(user_in):
   number1 = 0
   number2 = 0
   for c in user_in:
       if c in ['*','/','+','-']:
           number1 = float(''.join(user_in[:user_in.index(c)]))
           number2 = float(''.join(user_in[user_in.index(c)+1:]))
           operator = user_in[user_in.index(c)]

           return(number1,number2,operator)


def get_input():
   userinput = list(input("Please enter an expression"))
   return(userinput)

def doCalc(number1, number2, operator):

           if operator == "+":
               result = number1 + number2
           elif operator == "*":
               result = number1 * number2
           elif operator == "-":
               result = number1 - number2
           elif operator == "/":
               try:
                   result = number1 / number2
               except:
                   result = "Undefined"
                   print("Unable to divide by Zero!")

           print("The result is " + str(result) + ".\n")

def main():
   user_in = get_input()
   number1, number2, operator = getPieces(user_in)
   doCalc(number1,number2,operator)

main()


