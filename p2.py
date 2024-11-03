# find the product of all proper factors of a number
def product(x): #we create this function to find the proper factors of a number and their product
    if x==0: #particular case
        return 0
    d = 2 #variable for all possible factors of the number
    p = 1 #variable for the product
    while x > 1: #until x can not be divisible with other factors
        k = 0 #variable for counting how many times x is divisible by d
        while x % d == 0:
            x = x // d
            k = k + 1
        if k != 0: #if d divided x at least one time then we multiply d to the product
            p = p * d
        d = d + 1 #we go to the next possible factor
        if d * d > x: #if d is greater than sqrt(x) then we finish the program(all factors are smaller or equal to sqrt(x))
            d = x
    return p #return the product
def main():
    x = int(input("Write a natural number:"))
    result=product(x)
    print("The product of all the proper factors of your number is:", result)
if __name__ == "__main__":
    main()

