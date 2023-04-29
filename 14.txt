# 14.A program to print the Fibonacci series.
def fibonacci(n):

    fib_series = [0, 1]


    while fib_series[-1] + fib_series[-2] <= n:
        next_number = fib_series[-1] + fib_series[-2]
        fib_series.append(next_number)

    return fib_series

n = int(input("enter the num to find its fibonacci :"))
fib_series = fibonacci(n)
print(fib_series)
