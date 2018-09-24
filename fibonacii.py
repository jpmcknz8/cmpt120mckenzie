# fibonacii.py
# Computes the nth number of a given input

def main():
    # returns the nth fibonacci number
    current = 1
    holder=1
    previous = 1
    n=int(input("Please enter a whole number:"))
    for i in range(1, n-1):
        
        holder= current+ previous
        current = previous
        previous = holder
    print(holder)
main() 
