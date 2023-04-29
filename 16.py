# 16.Write a program to find the sum of all the multiples of 3 or 5 below a given number.

def sum_of_multiples(n):
   
    sum_of_multiples = 0

    
    for i in range(1, n):
        if i % 3 == 0 or i % 5 == 0:
            sum_of_multiples += i

    return sum_of_multiples


n = int(input("enter the limit :"))
sum = sum_of_multiples(n)
print(f"The sum of all multiples of 3 or 5 below {n} is {sum}.")
