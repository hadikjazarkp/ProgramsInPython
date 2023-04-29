
# 9.Write a function to generate all prime numbers up to a given limit

def generate_primes(limit):
   
    primes = [True] * (limit + 1)  
    primes[0] = primes[1] = False 
    
    for i in range(2, int(limit /2) + 1):
        if primes[i]:
            for j in range(i * i, limit + 1, i):
                primes[j] = False
    
    return [i for i in range(2, limit + 1) if primes[i]]


limit = int(input("enter a num to find the prime num limit :"))
primes = generate_primes(limit)
print(primes)
