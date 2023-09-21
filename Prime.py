def prime(n):
    counter=0
    for i in range(2,n//2+1):
        if (n%i==0):
            counter=1
            break
    if (counter==1):
        print("It is not a prime number")
    else:
        print("It is a prime number")
#__main__
x=int(input("Enter the number "))
prime(x)

