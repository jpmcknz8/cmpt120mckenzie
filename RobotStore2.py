# RobotStore2.py

class Product:

    def __init__(self,name, price, quantity):
        self.name = name
        self.price = float(price)
        self.quantity = float(quantity)

    def stock(quantity, price):
        if self.quantity >= count:
            return(True)
        else:
            return(False)
    def totalCost(quantity, price):
        totalCost = self.price * count
        return totalCost

def createProduct(inforStr):
    name, price, quantity = inforStr("\t")
    return Product(name, price, quantity)


productNames = [ "Ultrasonic range finder",
                 "Servo motor",
                 "Servo controller",
                 "Microcontroller Board",
                 "Laser range finder",
                 "Lithium polymer battery"]
productPrices = [ 2.50, 14.99, 44.95, 34.95, 149.99, 8.99 ]
productQuantities = [ 4, 10, 5, 7, 2, 8 ]

Product = [Product("Ultrasonic range finder", 2.50, 4),
           Product("Servo Motor", 14.99, 10),
           Product("Servo Controller", 44.95, 5),
           Product("Microcontroller Board", 34.95, 7),
           Product("Laser Range Finder", 149.99, 2),
           Product("Lithium Polymer Battery", 8.99, 8)]

def findCount():
    count = input ("Enter the amount of product you would purchase: ")

def printStock():
    print()
    print("Available Products")
    print("------------------")
    for i in range(0,len(productNames)):
        if productQuantities[i] > 0:
            print(str(i)+")",productNames[i], "$", productPrices[i])
    print()

def main():
    cash = float(input("How much money do you have? $"))
    while cash > 0:
        printStock()

        vals = input("Enter product ID and quantity you wish to buy: ").split(" ")

        if vals[0] == "quit": break

        prodId = int(vals[0])
        count = int(vals[1])

        if productQuantities[prodId] >= count:
            if cash >= productPrices[prodId]:
                productQuantities[prodId] -= count
                cash -= productPrices[prodId] * count
                print("You purchased", count, productNames[prodId]+".")
                print("You have $", "{0:.2f}".format(cash), "remaining.")
            else:
                print("Sorry, you cannot afford that product.")
        else:
           print("Sorry, we are sold out of", productNames[prodId])



main()
