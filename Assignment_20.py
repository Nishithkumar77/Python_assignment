# More on functions

# 1. Write a python program to create a function that takes a list and returns a new list with the original list's unique elements.

def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x
l= [1,2,3,3,3,3,4,5]
print(unique_list(l))

# 2. Write a python program to create a function that takes a number as a parameter and checks if the number is prime or not.

def prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True;
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True
n=int(input("Enter the number: "))
print(prime(n))

# 3. Write a python program to create a function that prints the even numbers from a given list.
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]

def is_even_num(list):
    enum = []
    for n in list:
        if n % 2 == 0:
            enum.append(n)
    return enum
print(is_even_num([1, 2, 3, 4, 5, 6, 7, 8, 9]))

# 4. Write a python program to create a function that checks whether a passed string is palindrome or not.

def is_palindrome(string):
    return string == string[::-1]
string = input("Enter a string: ")
ans=is_palindrome(string)

if ans:
    print("Palindrome")
else:
    print("Not Palindrome")

# 5. Write a python program to create a function to find the Min of three numbers.

def max_of_two( x, y ):
    if x > y:
        return x
    return y
def max_of_three( x, y, z ):
    return max_of_two( x, max_of_two( y, z ) )
print(max_of_three(3, 6, -5))

# 6. Write a python program to create a function and print a list where the values are square of numbers between 1 and 30.

def printValues():
	l = list()
	for i in range(1,29):
		l.append(i**2)
	print(l)
		
printValues()

# 7. Write a python program to access a function inside a function.

def test(a):
        def add(b):
                nonlocal a
                a += 1
                return a+b
        return add
func= test(4)
print(func(4))

# 8. Write a python program to create a function that accepts a string and calculate the number of upper case letters and lower case letters.

def string_test(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])
s= input("Enter the string: ")
string_test(s)

# 9. Write a python program to create a function to check whether a string is a pangram or not.

import string
  
alphabet = set(string.ascii_lowercase)
  
def ispangram(string):
    return set(string.lower()) >= alphabet
      
string = input("Enter the string: ")
if(ispangram(string) == True):
    print("Yes")
else:
    print("No")

# 10. Write a python program to create a function to check whether a string is an anagram or not.

def is_anagram(s1, s2):
    return set(s1) == set(s2)
print(is_anagram("elvis","lives"))
