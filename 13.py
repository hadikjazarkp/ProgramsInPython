# 13.Write a function to check if a given number is an Armstrong number.

def is_armstrong_number(n):
    
    
    num_digits = len(str(n))

    
    sum_of_cubes = 0
    for digit in str(n):
        sum_of_cubes =sum_of_cubes + int(digit) ** num_digits
    return sum_of_cubes == n
    
n = int(input("enter a num to check it is armstrong or not "))
if is_armstrong_number(n):
    print(f"{n} is an Armstrong number.")
else:
    print(f"{n} is not an Armstrong number.")
