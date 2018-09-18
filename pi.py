# pi.py
# A program that approximates the value of pi by summing a sequence
import math


n = input("Enter the amount of terms to calculate the sum")
def main():
    sum = 0.0
    for i in range(1,int(n)+1, 4):
        sum = sum + (4/i)-(4/(i+2))
        print(sum)

main()

    
