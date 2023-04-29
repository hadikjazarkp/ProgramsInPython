# 4.Write a function to calculate the sum of all even numbers between 1 and n.


def calculate_sum_of_even(num):
    sum=0
    for elem in range(0,num+1,2):
        sum=sum+elem
    print(sum)
num=10 
calculate_sum_of_even(num)
