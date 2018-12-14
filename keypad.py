# keypad.py
from button import *

class Keypad:
    def __init__(self, win):
        self.buttons = [
            Button(win, Point(1,1), .5, .5, '-/+'),
            Button(win, Point(1.75,1), .5, .5, '0'),
            Button(win, Point(2.5,1), .5, .5, '.'),
            Button(win, Point(3.25,1), .5, .5, '='),
            Button(win, Point(4,1), .5, .5, 'mr'),
            Button(win, Point(4,1.75), .5, .5, '('),
            Button(win, Point(4,2.5), .5, .5, ')'),
            Button(win, Point(4,3.25), .5, .5, 'cos'),
            Button(win, Point(4,4), .5, .5, 'sin'),
            Button(win, Point(1,1.75), .5, .5, '1'),
            Button(win, Point(1.75,1.75), .5, .5, '2'),
            Button(win, Point(2.5,1.75), .5, .5, '3'),
            Button(win, Point(3.25,1.75), .5, .5, '+'),
            Button(win, Point(1,2.5), .5, .5, '4'),
            Button(win, Point(1.75,2.5), .5, .5, '5'),
            Button(win, Point(2.5,2.5), .5, .5, '6'),
            Button(win, Point(3.25,2.5), .5, .5, '-'),
            Button(win, Point(1,3.25), .5, .5, '7'),
            Button(win, Point(1.75,3.25), .5, .5, '8'),
            Button(win, Point(2.5,3.25), .5, .5, '9'),
            Button(win, Point(3.25,3.25), .5, .5, 'x'),
            Button(win, Point(1,4), .5, .5, 'del'),
            Button(win, Point(1.75,4), .5, .5, 'm+'),
            Button(win, Point(2.5,4), .5, .5, 'm-'),
            Button(win, Point(3.25,4), .5, .5, '/'),
            Button(win, Point(4,4.75), .5, .5, 'tan'),
            Button(win, Point(.35,4), .5, .5, 'asin'),
            Button(win, Point(.35,3.25), .5, .5, 'acos'),
            Button(win, Point(.35,2.5), .5, .5, 'atan')
            ]

    def getKey(self, p):
        for button in self.buttons:
            if button.clicked(p):
                return (button.getLabel())
