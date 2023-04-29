# 12.Write a function to check given string is palindrome or not.
def is_palindrome(s):
    s=s.lower()
    return s == s[::-1]

s = input("enter a num to check its palidrome :")
if is_palindrome(s):
    print("The string is  palindrome.")
else:
    print("The string is not  palindrome.")
