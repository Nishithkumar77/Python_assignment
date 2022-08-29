# 1. Write a python script to check whether a given number is positive or non-positive


number = int(input("Enter the number: "))

if number>0:
    print("Positive")
else:
    print("Non Positive")

# 2. Write a python script to check whether a given number is divisible by 5 or not


num = int(input("Enter the number: "))

if num%5==0:
    print("Divisible by 5")
else:
    print("Not Divisible")

# 3. Write a python script to check whether a given number is even or odd


num1 = int(input("Enter the number: "))

if num%2==0:
    print("Even")
else:
    print("Odd")

# 4. Write a python script to print greater between two numbers. Print number only once even if the numbers are the same.


number1 = int(input("Enter the number: "))
number2 = int(input("Enter the number: "))

if number1 > number2:
    print("number1 is greater than number2")
else:
    print("number2 is greater than number1")

# 5. Write a python script to print two given words in dictionary order.

print(input())
a,b=input(),input()
print((b,a) if a>b else(b,a))

# 6. Write a python script to check whether a given number is a three digit number or not.

num1=int(input("Enter your number:"))
if(num1 < 1000 and num1 > 99):
    print("Number is a 3 digit number ",num1)
else:
    print("Number is not a 3 digit number",num1)



# 7. Write a python script to check whether a given number is positive, negative or zero.

a = int(input("Enter the number: "))
if a>0:
    print("Positive")
elif a<0:
    print("Negative")
else:
    print("Zero")

# 8. Write a python script to check whether a given quadratic equation has two real & distinct roots, real & equal roots or imaginary root.

print(enter a value a,b and c of equation)
a,b.c=int(input)
d=b**2-4*a*c
if d>0:
    print("Real and distinct root")
elif d==0:
    print("Real and equal root")
else:
    print("Imaginary roots")
    
# 9. Write a python script to check whether a given year is a leap year or not.

year = int(input("Enter year:"))
if year%400==0 or year%100!=0 and year%4==0:
    print("Year is leap year")
else:
    print("Not a leap year")


# 10. Write a python script to print greater among three numbers. Print number only once even if the numbers are the same.

n1=float(input("Enter a number:"))
n2=float(input("Enter a number:"))
n3=float(input("Enter a number:"))
if n1>=n2 and n1>=n3:
    print("n1 is greater",n1)
elif n2>=n1 and n2>=n3:
    print("n2 is greater",n2)
else:
    print("n3 is greater",n3)

# 11. Write a python script to take the month value in numeric format and display the number of days in it.

month = int(input("Enter month number: "))
if month in (1,3,5,7,8,10,12):
    print("31 Days")
elif month in (4,6,9,11):
    print("30 Days")
elif month==2:
    print("28 or 29 Days")
else:
    print("Invalid month number")

# 12. Write a python script to accept one complex number from the user and display the greater number between real part and imaginary part.

x=complex(input("Enter a complex number: "))
print((x.real) if x.real>x.imag else print(x.imag))
