# 17.Write a program to find the sum of all the even or odd numbers below a given number.

def sum_of_numbers(n, even=True):

    sum_of_numbers = 0


    for i in range(n):
        if even and i % 2 == 0:
            sum_of_numbers += i
        elif not even and i % 2 != 0:
            sum_of_numbers += i

    return sum_of_numbers



n = int(input("enter the limit:"))
even_sum = sum_of_numbers(n)
odd_sum = sum_of_numbers(n, False)
print(f"The sum of all even numbers below {n} is {even_sum}.")
print(f"The sum of all odd numbers below {n} is {odd_sum}.")
