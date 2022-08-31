# 1. Write a python script to create a String in 3 different possible ways

my_string = 'Hello'
print(my_string)

my_string = "Hello"
print(my_string)

my_string = '''Hello'''
print(my_string)

# 2. Write a python script to Get the characters from the start to position 5 (Given String “iNeuron” using the slice syntax)

a="iNeuron"
print(a[:6])

# 3. Write a python script to Get the characters from position 2 to position 5 (Given String “Hello Learners” using the slice syntax)

b="Hello Learners"
print(b[2:6])

# 4. Write a python script to demonstrate String Concatenation adding space in between ( Given Strings a=”Learning” b=”Python” )

a="Learning"
b="Python"
c= ' '.join(a+b)
print(c)


# 5. Write a python script to get the count of total number of characters in String a= “iNeuron”

a="iNeuron"
print(len(a))


# 6. Write a python script to reverse a String. (“iNeuron”)

a="iNeuron"
print(a[::-1])

# 7. Write a python script to determine whether a string contains a specific substring.

string = input("Enter a string: ")
str = input("Subtring: ")
print(str in subtring)

# 8. Write a python script to check if a string contains only numbers.

str="12345"
print(str.isdigit())

# 9. Write a python script to check if a string contains only characters of the alphabet.

str = "MySirG"
print(str.isalpha())

# 10. Write a python script to convert an integer to a string.

num = int(input("Enter the number: "))
  
# check  and print type of num variable
print("Type of variable before convertion : ", type(num)) 
  
# convert the num into string and print
converted_num = "% s" % num
print("Type after convertion : ", type(converted_num))
