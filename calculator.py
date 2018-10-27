# calculator.py

def get_user_input():
    userinput = list(input("Please enter an expression"))
    parts =[]
    pointer1 = 0
    pointer2 = 0

    for c in userinput:
        if c in ['*','/','+','-']:
            parts.append(''.join(userinput[pointer1:userinput.index(c)]))
            parts.append(c)
            pointer1 = userinput.index(c) + 1
            #pointer2 = pointer1

            for i in userinput[pointer1:]:
                if i in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                    pointer2 +=1

                    if pointer2 == len(userinput):
                        pass
            parts.append(''.join(userinput[pointer1:]))
            print('hit for loop: pointer 1 = ' + str(pointer1))
            return(parts)

def main():
    expression_parts = get_user_input()
    print(expression_parts)
        
main()
