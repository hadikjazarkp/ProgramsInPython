# 15.Write a program to find the sum of all prime numbers up to a given limit.
def is_prime(n):
    
    for i in range(2, int(n /2) + 1):
        if n % i == 0:
            return False
    return True


def sum_of_primes(limit):
   
    sum_of_primes = 0

    for i in range(2, limit + 1):
        if is_prime(i):
            sum_of_primes += i

    return sum_of_primes

limit = int(input("enter the limit:"))
sum = sum_of_primes(limit)
print(f"The sum of all prime numbers up to {limit} is {sum}.")
