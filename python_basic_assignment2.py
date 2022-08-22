# Q1. # is used for adding comments
print("Learning Python")

"""
Q2. This is used for multi-line comment
"""
x = "Nishith"
y = 27
z = 2*4
a = 5.5
print(x,y,z,a,sep='\n')

# Q3.Write a python script to print types of variables. Create 5 variables each of them containing different types of data. (like 35, True, “MySirG”,5.46, 3+4j, etc)
 
a = 35
b = True
c = "MySirG"
d = 5.46
e = 3+4j
print(a,b,c,d,e)
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

# Q4.Write a python script to print the id of two variables containing the same integer values

x=10
y=10
print(id(x))
print(id(y))

"""
Q5. Create four variables in a Python script and assign values of different data types to
them. Write a Python script to print value, its type and id of each variable
"""
a1 = 10
print(a1)
print(type(a1))
print(id(a1))

a2 = "Ram"
print(a2)
print(type(a2))
print(id(a2))

a3 = 4.5
print(a3)
print(type(a3))
print(id(a3))

a4 = True
print(a4)
print(type(a4))
print(id(a4))

# Q6.Write a python script to print all the keywords

import keyword
print(keyword.kwlist)

# Q9.Name the keywords, used as data in the Python script.

# Ans.   True, False, None

"""
Q10.Write a python script to display the current date and time. First create variables to
store date and time, then display date and time in proper format (like: 13-8-2022 and
9:00 PM
"""

import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%d-%m-Y% and %H:%M %p"))
