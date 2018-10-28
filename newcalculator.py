# calculator.py

# JA: You need to connect the equation solving with the grqaphical interface
from graphics import *

win = GraphWin('Calculator', 400, 400)



def drawRec(p1, p2, p3, p4, color):
    tempRec = Rectangle(Point(p1, p2), Point(p3, p4))
    tempRec.setFill(color)
    return(tempRec)

def drawPoint(p1, p2, text, color):
    tempPoint = Text(Point(p1, p2), text)
    tempPoint.setTextColor(color)
    return(tempPoint)
    
calc = drawRec(20, 40, 325, 390,'black') 
calc.draw(win)
bar = drawRec(60,60,285,110,'grey')
bar.draw(win)



button7 = drawRec(75, 120, 120, 165, 'green')
button4 = drawRec(75, 170, 120, 215, 'green')
button1 = drawRec(75, 220, 120, 265, 'green')
buttonposneg = drawRec(75, 270, 120, 315,'green')
button8 = drawRec(125, 120, 170, 165, 'blue')
button5 = drawRec(125, 170, 170, 215, 'blue')
button2 = drawRec(125, 220, 170, 265, 'blue')
button0 = drawRec(125, 270, 170, 315, 'blue')
button9 = drawRec(175, 120, 220, 165, 'yellow')
button6 = drawRec(175, 170, 220, 215, 'yellow')
button3 = drawRec(175, 220, 220, 265, 'yellow')
buttondot = drawRec(175, 270, 220, 315, 'yellow')
buttondel = drawRec(175, 320, 220, 365, 'yellow')
buttondiv = drawRec(225, 120, 270, 165, 'brown')
buttonmult = drawRec(225, 170, 270, 215, 'brown')
buttonadd = drawRec(225, 220, 270, 265, 'brown')
buttonsub = drawRec(225, 270, 270, 315, 'brown')
buttonequal = drawRec(225, 320, 270, 365, 'brown')

button7.draw(win) 
button4.draw(win)
button1.draw(win)
buttonposneg.draw(win)
button8.draw(win)
button5.draw(win)
button2.draw(win)
button0.draw(win)
button9.draw(win)
button6.draw(win)
button3.draw(win)
buttondot.draw(win)
buttondel.draw(win) 
buttondiv.draw(win) 
buttonmult.draw(win)
buttonadd.draw(win)
buttonsub.draw(win) 
buttonequal.draw(win)


character7 = drawPoint(97.5, 142.5, '7', 'white')
character4 = drawPoint(97.5, 192.5,'4', 'white')
character1 = drawPoint(97.5, 242.5, '1', 'white')
characterposneg = drawPoint(97.5, 292.5, '+/-', 'white')
character8 = drawPoint(147.5, 142.5, '8', 'white')
character5 = drawPoint(147.5, 192.5, '5', 'white')
character2 = drawPoint(147.5, 242.5, '2', 'white')
character0 = drawPoint(147.5, 292.5, '0', 'white')
character9 = drawPoint(197.5, 142.5, '9', 'white')
character6 = drawPoint(197.5, 192.5, '6', 'white')
character3 = drawPoint(197.5, 242.5, '3', 'white')
characterdot = drawPoint(222.5, 292.5, '.', 'white')
characterdel = drawPoint(197.5, 342.5, 'del', 'white')
characterdiv = drawPoint(247.5, 142.5, '/', 'white')
charactermult = drawPoint(247.5, 192.5, '*', 'white')
characteradd = drawPoint(247.5, 242.5, '+', 'white')
charactersub = drawPoint(247.5, 292.5, '-', 'white')
characterequal = drawPoint(247.5, 342.5, '=', 'white')

character7.draw(win)
character4.draw(win)
character1.draw(win)
characterposneg.draw(win)
character8.draw(win)
character5.draw(win)
character2.draw(win)
character0.draw(win)
character9.draw(win)
character6.draw(win)
character3.draw(win)
characterdot.draw(win)
characterdel.draw(win)
characterdiv.draw(win)
charactermult.draw(win)
characteradd.draw(win)
charactersub.draw(win)
characterequal.draw(win)


def main():
    equation = input("Please enter an equation (use spaces):")
    listEquation = equation.split()
    result = solveEquation(listEquation)
    print(result)

def modifyEquation(idx, eq, value):
    # remove the two operands and the operqator
    del eq[idx - 1:idx + 2]
    # insert the result
    eq.insert(idx - 1, value)
    # move the index back one place
    idx = idx - 1
    return idx, eq
    
def solveEquation(eq):
    opIdx = 1
    while '*' in eq or '/' in eq:
        if eq[opIdx] == '*':
            # calculate the operation
            result = float(eq[opIdx - 1]) * float(eq[opIdx + 1])
            # update the equation list
            opIdx, eq = modifyEquation(opIdx, eq, result)
        elif eq[opIdx] == '/':
            result = float(eq[opIdx - 1]) / float(eq[opIdx + 1])
            opIdx, eq = modifyEquation(opIdx, eq, result)
        else:
            opIdx = opIdx + 1    
        if opIdx >= len(eq):
            break
    opIdx = 1 
    while '+' in eq or '-' in eq:
        if eq[opIdx] == '+':
            result = float(eq[opIdx - 1]) + float(eq[opIdx + 1])
            opIdx, eq = modifyEquation(opIdx, eq, result)
        elif eq[opIdx] == '-':
            result = float(eq[opIdx - 1]) - float(eq[opIdx + 1])
            opIdx, eq = modifyEquation(opIdx, eq, result)
        else:
            opIdx = opIdx + 1
        if opIdx >= len(eq):
            break
    return eq[0]
            
main()
