def factorial(n):
    fac: int=1
    for i in range(n):
        fac=fac *(i+1)
    print("Factorial is",fac)
n = int(input("Enter a number : "))
factorial(n)