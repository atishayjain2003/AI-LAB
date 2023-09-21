def factorial(n):
    product=1
    while(n>=1):
        product*=n
        n-=1
    print("The factorial is", product)
#__main__
x=int(input("Enter number"))
factorial(x)