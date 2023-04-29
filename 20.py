# 20.Write a program to count the number of vowels in a given string.

def count_vowels(string):
   
    
    vowels = set("aeiouAEIOU")

   
    vowel_count = 0

  
    for char in string:
        if char in vowels:
            vowel_count += 1

    return vowel_count


string = "Hello, World!"
vowel_count = count_vowels(string)
print(f"There are {vowel_count} vowels in the string '{string}'.")
