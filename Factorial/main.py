def recur_factorial(n):
    if n == 1:
        return n
    else:
        return n*recur_factorial(n-1)
    
num = int(input("enter a Number: "))

if num < 0:
    print("Sorry, Factorial does not exist for negative numbers.")
elif num == 0:
    print("The Factorial of 0 is 1.")
else:
    print("The Factorial of ", num,"is", recur_factorial(num))