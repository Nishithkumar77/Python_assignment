# 1. Write a python script to take your name as input from the user and then print it.

Name = input("Enter Name: ")
print("Your name is: ",Name)

# 2. Write a python script to take input from the user. Input must be a number.

num = int(input("Enter number: "))
print(num)

# 3. Write a python script which takes two numbers from the user, then calculate their sum and display the result.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
sum = num1 + num2
print("Sum is: ",sum)

# 4. Write a python script which takes the radius from the user and display area of a circle.

r = float(input("Enter the radius: "))
p = 3.14  # pie
area = p*r**2
print("Area Of Circle is: ",area)

# 5. Write a python script to calculate the square of a number. Number is entered by the user.

s = float(input("Enter the number: "))
square = s**2
print("Square of a number is: ",square)

# 6. Write a python script to calculate the area of Triangle. Number is entered by the user.

base = int(input("Enter the base: "))
height = int(input("Enter the height: "))
area_of_triamgle = 1/2*base*height
print("Area of Triangle is: ",area_of_triamgle)

# 7. Write a python script to calculate average of three numbers, entered by the user.

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
avg = (a+b+c)/3
print("Average is: ",avg)

# 8. Write a python script to calculate simple interest.

principal = int(input("Enter the Principal: "))
rate = int(input("Enter the ROI: "))
time = int(input("Enter the Time: "))

si = (principal*rate*time)/100
print("Simple Interest",si)

# 9. Write a python script to calculate the volume of a cuboid.

length = int(input("Enter the length: "))
width = int(input("Enter the second width: "))
height = int(input("Enter the third height: "))

cuboid = length*width*height
print("Volume of a cuboid: ",cuboid)

# 10. Write a python script to calculate area of a rectangle

len = int(input("Enter the length: "))
wid = int(input("Enter the width: "))
area_of_rectangle = len*wid
print("area of rectangle: ",area_of_rectangle)
