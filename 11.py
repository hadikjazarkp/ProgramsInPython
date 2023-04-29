# 11.Write a function to calculate the factorial of a given number n

def calculate_factorial(n):
   
    if n == 0:  
        return 1
    else: 
        for i in range(1,n):
            n=n*i
        return  n

n = int(input("enter a num to find its factorial:"))
factorial = calculate_factorial(n)
print("the factorial is :",factorial) 
