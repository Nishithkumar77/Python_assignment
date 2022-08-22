# Q1. Write a python script to convert a number into str type.


x = 10
y = str(x)
print(type(y))

# Q2. Write a python script to print Unicode of the character ‘m’

z = 'm'
print(ord(z))

# Q3. Write a python script to print character representation of a given unicode 100.


a = 100
print(chr(a))


# Q4. Write a python script to print any number and its binary equivalent

num = int(input("Enter the number: "))
print(bin(num))

# Q5. Write a python script to print any number and its octal equivalent

num1 = int(input("Enter the number: "))
print(oct(num1))

# Q6. Write a python script to print any number and its hexadecimal equivalent.

num2 = int(input("Enter the number: "))
print(hex(num2))

# Q7. Write a python script to store binary number 1100101 in a variable and print it in decimal format.

b = 0b1100101
print("Binary to Decimal", b, ":", b)

# Q8. Write a python script to store a hexadecimal number 2F in a variable and print it in octal format.
C = 0x2F
print("Hexadecimal to Octal", C, ":", oct(C))

# Q9.Write a python script to store an octal number 125 in a variable and print it in binary format.

d = 0o125
print("Octal to Binary", d, ":", bin(d))


# Q10.Write a python script to add two numbers 25 (in octal) and 39 (in hexadecimal) and display the result in binary format.

num1 = 25
num2 = 39
sum = (bin(num1)+bin(num2))
print("Binary is: ", sum)
