# Match Case Assignment
# 1. Write a python script to display the number of days in a given month number.

month = int(input("Enter the month number: "))
match month:
    case month if month in(1,3,5,7,8,10,12):
        print("31 days")
    case month if month==2:
        print("28 or 29 days")
    case month if month in(4,6,9,11):
        print("30 days")
    case _:
        print("Invalid Month number")
        
# 2. Write a menu driven program to perform following operations - Addition, Subtraction, Multiplication, Division

print("1. Addition")
print("2. Subtraction")
print("3. Multlipication")
print("4. Division")
choice = int(input("Enter your choice: "))
match choice:
    case 1:
        print("Enter the two number: ")
        a,b=int(input()),int(input())
        c=a+b
        print("Sum is: ",c)
    case 2:
        print("Enter the two number: ")
        a,b=int(input()),int(input())
        c=a-b
        print("Difference is: ",c)
    case 3:
        print("Enter the two number: ")
        a,b=int(input()),int(input())
        c=a*b
        print("Multiply is: ",c)
    case 4:
        print("Enter the two number: ")
        a,b=int(input()),int(input())
        c=a/b
        print("Division is: ",c)
    case _:
        print("Invalid")
        
# 3. Write a menu driven program with the following options:
# a. Check whether a given set of three numbers are lengths of an isosceles triangle or not
# b. Check whether a given set of three numbers are lengths of sides of a right angled triangle or not
# c. Check whether a given set of three numbers are equilateral triangle or not
# d. Exit.

side1 = int(input("Enter side1: "))
side2 = int(input("Enter side2: "))
side3 = int(input("Enter side3: "))
match (side1,side2,side3):
    case (side1,side2,side3) if side1 == side2 == side3:
        print("Equilateral Triangle")
        
    case (side1,side2,side3) if side1 == side2 or side2 == side3 or side3 == side1:
        print("Isosceles Triangle")
    case (side1,side2,side3) if side1!=side2 or side2!=side3 or side1!=side3:
        print("Scalene Triangle")
    case _:
        exit()

# 4. Write a program which takes user’s age and display the category of person. Age below 10 years- Kid, Age below 20 - Teen, Age below 40 - young, Age below 60 -
# Experienced, Age above or equal 60 - Senior Citizen.

age = int(input("Enter your age: "))
match age:
    case age if age<10:
        print("You are Kid")
    case age if age<20:
        print("You are Teen")
    case age if age<40:
        print("You are Young")
    case age if age<60:
        print("You are Experienced")
    case age if age>=60:
        print("You are senoir citizen")
        
# 5. Write a program which takes a number from user. Print Saurabh Shukla if the number is even, print Prateek Jain if the number is negative odd number and print Aditya
# Choudhary if number is positive odd number.

num = int(input("Enter a number: "))
match num:
    case num if num%2==0:
        print("Saurabh Shukla")
    case num if num<0 and num%2:
        print("Prateek Jain")
    case num if num>0 and num%2:
        print("Aditya Chaudhary")
        
# 6. Write a python program to check whether a given string is a multiword string or single word string using match case statement

str = input("Enter a string: ")
str.strip()
match str:
    case str if ' ' in str:
        print("Multiword string")
    case str if ' ' not in str:
        print("Single word string")
        
# 7. Write a python program to check whether a given number is positive, negative or zero using match case statement

num1 = int(input("Enter a number: "))
match num1:
    case num1 if num1>0:
        print("Positive")
    case num1 if num1<0:
        print("Negative")
    case _:
        print("Zero")
        
# 8. Write a python script to check whether two given strings are identical, first string comes before the second in dictionary order or first string comes after the second
# string in dictionary order using match case statement.

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
match (str1,str2):
    case (str1,str2) if str1==str2:
        print("Strings are identical")
    case (str1,str2) if str1>str2:
        print("{} comes before {} ".format(str1,str2))
    case (str1,str2) if str1<str2:
        print("{} comes after {}".format(str2,str1))

# 9. Write a python script to check whether a given year is
'''
a. Non century leap year
b. Century leap year
c. Non century non leap year
d. Century non leap year
'''
year = int(input("Enter year: "))
match year:
    case year if year%4!=0 and year%100!=0:
        print("Non centuary non leap year")
    case year if year%100!=0:
        print("Non century leap year")
    case year if year%400==0:
        print("Century leap year")
    
# 10. Write a program to display day name on the basis of user’s liking of a colour. Ask user for his favorite colour. User can answer in a sentence like “I like red colour”.
# Assuming all colour name entered by user is in lowercase. Use match case to display day name associated with the colour.
'''
a. Yellow - Monday
b. Blue - Tuesday
c. Orange - Wednesday
d. White - Thursday
e. Black - Friday
f. Red - Saturday
g. All other colours - Sunday
'''

string = input("Enter a string: ")
list = ["yellow","blue","orange","white","black","red","other"]
for color in list:
    if color in string:
        c=color
        break
    else:
        c="other"
match c:
    case "yellow":
        print("Monday")
    case "blue":
        print("Tuesday")
    case "orange":
        print("Wedneday")
    case "white":
        print("Thursday")
    case "black":
        print("Friday")
    case "red":
        print("Saturday")
    case "other":
        print("Sunday")
