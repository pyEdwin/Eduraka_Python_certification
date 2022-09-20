#!/usr/bin/env python
# coding: utf-8

# Write a program to find the factors of agiven number and check whether the factor is even or odd.
# 
# Hint: Use Loop with if-else statements

# In[14]:


number = int(input("Enter a number:"))
odd = []
even = []
for i in range (1 , (number +1)):
    if number % i == 0 and i % 2 ==0:
        even.append(i)
    else:
        odd.append(i)
print("Factors of", number, ", which are even:", end=" ")
print(even)
        
print("Factors of",number,", which are odd:", end=" ")
print(odd)


# Write a code that accepts a sequence of words as input and prints the words in a sequence after sorting them alphabetically.
# 
# Hint: Use split() to split the string into a list and then apply sort()

# In[4]:


string = input("Enter a sequence: ")
string_split = string.split(" ")
string_split.sort()
print(string_split)


# Write a program that will find all the numbers between 1000 and 3000 (both excluded) such that each digit of a number is an odd number. 
# 
# Print the number of such elements

# In[12]:


list_of_odd_numbers = []
list_of_even_numbers = []
for i in range(999 , 3001):
    if i > 1000 and i < 3000 and i%2 != 0:
        list_of_odd_numbers.append(i)
    #else:
        #list_of_even_numbers.append(i)
#print("List of even numbers:", end=" ")
#print(list_of_even_numbers)

print("List of odd numbers:", end=" ")
print(list_of_odd_numbers)
        


# Write a program that accepts a stringand calculatesthe number of letters and digits. 
# 
# Suppose if the entered string is: Edureka123
# 
# Then the output will be: 
# 
# LETTERS: -7 
# DIGITS: -3

# In[16]:


letters_count = 0
digits_count = 0
number = '0123456789'
alphabet ='abcdefghijklmnopqrstuvwxyz'
capital_alphabet='ABCDEFGHIJKLMNOPRSTUVWXYZ'
word = input("Enter a word: ")
for i in word:
    if i in alphabet or i in capital_alphabet:
        letters_count +=1
    else:
        digits_count +=1
        
print("LETTERS:",end=" -")
print(letters_count)

print("DIGITS:",end=" -")
print(digits_count)


# Design a code which will find whether the given number is Palindrome number or not.

# In[25]:


number = int(input("Enter a number"))
number_to_string = str(number)
reverse_number = number_to_string[::-1]
if number_to_string == reverse_number:
    print(number , " is Palindrome.")
else:
    print(number," is not Palidrome")


# In[ ]:




