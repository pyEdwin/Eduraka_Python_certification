#!/usr/bin/env python
# coding: utf-8

# Smith wishes to register ona ticket booking website for booking bus tickets. To authenticate
# 
# the registration, he needs to provide a user-id and password. There are some built-in rules for 
# 
# checking the validity of the passwords entered by the users.Following are the rules for checking the
# 
# validity of a password:
# 
# i.At least 1 alphabet
# 
# ii.At least 1 digitbetween [0–9]
# 
# iii.At least 1 character from [@&]
# 
# iv.Minimum length of transaction password: 5
# 
# v.Maximum length of transaction password: 10

# In[4]:


digits_count=0
characters_count =0
password_lengh_count =0
number ="0123456789"
password = input("Enter your password:")

for i in range(len(password)):
    if password[i] in number:
        digits_count+=1
    elif password[i] in "@&":
        characters_count+=1
if digits_count >=1 and characters_count >=1 and len(password)>= 5 and len(password)<=10:
    print("Password created successfully.")
else:
    print("check password requirements")


# Write a program for printing all elements of a list and their indexes in the list.
# 
# Take the list as user input.

# In[ ]:


lst = list(input("Enter your elements here:"))
index_count = 0

for i in range(len(lst)):
   
    print("index: {} |  value: {}".format(index_count + i,lst[i]))


# In[ ]:





# Write  a  program that accepts a  string from the  console and prints the  characters that have even 
# 
# indexes if the character is an alphabet. Concatenate the characters and print.
# 
# Example If the following string is given as input to the program:Ed12ur3ka1Python12
# 
# Then, the output of the program should be:EuaPto

# In[6]:


string  = input("Enter your string here:")
string_concatinate=""
number="0123456789"
for i in range(len(string)):
    if i % 2==0 and string[i] not in number:
        string_concatinate+=string[i]  
print(string_concatinate)


# Please  write  a  program that accepts  a  string  from the console  and  prints it  in reverse order.
# 
# Example If the following string is given as input to the program: welcome to edureka Then, 
# 
# the output of the program should be: akerude ot emoclew

# In[8]:


string  = input("Enter your string here:")
string_reverse = string[::-1]
print(string_reverse)


# Please write a program that countsand prints the numbers of each character in a string input by the console.
# 
# Example If the following string is given as input to the program:abcdefgabcThen, 
# 
# the output of the program should be:
# a,2
# c,2
# b,2
# e,1
# d,1
# g,1
# f,1

# In[17]:


s = input("Enter you input here: ")
x=0
z={}
count=0
for i in range(len(s)):
    for a in s:
        if a == s[i]:
            count+=1
            z[a]=count
    count=0 
for i , x in z.items():
    print("{} , {}".format(i,x))


# With  two  given  lists  [1,5,10,12,34,13]  and  [4,7,8,10,5,13,24],  write  a  program  to create a 
# 
# new list whose elements are the intersection of the above-givenlists.

# In[18]:


list_1 = [1,5,6,12,34,13]
list_2 =[4,7,8,10,5,13,24]
list_2_sliced = list_2[:len(list_2)-1]
list_2_last_elmt = list_2[-1]
intersection_lists =[]

for i in range(len(list_2_sliced)):
    for a in list_1:
        if a == list_2_sliced[i] or a == list_2_last_elmt:
            intersection_lists.append(a)
print(intersection_lists )


# By using list comprehension, please write a program to print the list after removing the values which
# 
# are divisible by 6 in [12,24,35,24,88,120,155]

# In[21]:


lst = [12, 24 ,35 ,24 , 88 ,120, 155]
numbers_divisible_by_6 = [x for x in lst if x % 2 !=0]
print(numbers_divisible_by_6)


# By using list comprehension, please write a program to print the list after removing the 1st,3rd,and
# 
# 5thnumbers in [12,24,35,70,88,120,155].

# In[24]:


lst = [12, 24 ,35 ,24 , 88 ,120, 155]
number = (1,3,5)
new_list = [lst[i] for i in range(len(lst)) if i not in number]
print(new_list)


# Please  write  a  program  to  randomly  generate  a  list  with 6 numbers,  which  are divisible by 5 
# 
# and 7, between 1 and 1500 inclusive.

# In[26]:


import random
count = 0
lst=[]

for i in range(1 , 1501):
    if i % 5== 0 and i % 7 == 0 and i <=1500:
        lst.append(i)
        count+=1

ran = random.choices(lst, k=6)
print(ran)


# Write  a  program  to  compute  1/2+2/3+3/4+...+n/n+1  with  a  given  n  input  by console
# 
# (n>0).Example If the following n is given as input to the program:5 Then, 
# 
# the output of the program should be:3.55

# In[27]:


number = int(input("Enter your number"))
count = 0
if number > 0:
    for i in range(1 , number+1):
        count+=i/(i+1)
    print(round(count,2))
else:
    print("number should not be Negative")


# Case Study 
# 
# Domain: Banking
# 
# Focus:OptimizationBusiness 
# 
# challenge/requirement 
# 
# FinBank is the latest entrant in the banking market of Thailand.  
# 
# The verification process for opening a bank account is done manually by reviewing the photocopy of the
# 
# approved ID card. However, they have recently introduced a system where the customers’ fingerprints 
# 
# will be mapped with the newly introduced Unique ID for citizens of Thailand by the government.
# 
# FinBankshould implement a system that verifies customers against theirfingerprintsand Unique Id. 
# 
# Key issues Build a system where when a user enters a Unique ID,it gets encrypted so that hackers 
# 
# cannot view the mapping of the Unique ID and fingerprint.ConsiderationsThe system should be 
# 
# secure.
# 
# Data volume
# -NA
# 
# Additional information
# -NA
# 
# Business benefits
# 
# The bank will be able to verify customers’ data quickly, and the expected gain in volume is approximately ten times as the manual process of verification is replaced with asecure automated
# 
# system.
# 
# Approach to solve
# 
# 1.Read the input from the command line –UniqueID.
# 
# 2.Check for validityof Unique ID–it should be 10 digits and must containonly numbers.
# 
# 3.Encrypt the UniqueID and print it.
# 
# Enhancements for code
# 
# You can try these enhancements in code.
# 
# 1.Allow alphabets and some special characters in Unique ID
# 
# 2.Providethe option for decryption to the user.
# 

# In[28]:


import base64

lower_case_aphabet ="abcdefghijklmnopqrstuvwxyz"
capital_case_alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers ='1234567890'
digit_len = 0
numbers_checked = False
len_checked = False
unique_id = input("Enter your Unique ID.it should be 10 numbers: ")
alphabet_checked = False
uniqueid_valid = False

#check for alphabet letters
for i in range(len(unique_id)):
    if unique_id[i] in lower_case_aphabet or unique_id[i] in capital_case_alphabet:
        alphabet_checked = True
        break
    #else:
        #alphabet_checked = False
    if unique_id[i] in numbers:
        numbers_checked=True
    else:
        numbers_checked=False

if(len(unique_id)<= 10):
   len_checked = True
else:
    len_checked=False

if(alphabet_checked == False and numbers_checked== True and len_checked == True):
    print("Valid ID")
    uniqueid_valid = True
else:
    print("Try again")
if uniqueid_valid:
    uniqueid_encrypted = base64.b64encode(unique_id.encode())
    print("Encrypted unique id: {}.".format(uniqueid_encrypted))

    uniqueid_decrypted = base64.b64decode(uniqueid_encrypted )
    print("Decrypted unique id: {}.".format(uniqueid_decrypted))


# In[ ]:




