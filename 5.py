
# 5.Write a function to check if a given number is prime.


def prime_num(num):
    count=0
    for elem in range(1,num+1):
        if num % elem == 0  :
            count+=1
    if count==2:
        print("prime number")
    else:
        print("not prime num")
    
num=int(input("enter a number"))

prime_num(num)


