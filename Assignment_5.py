# 1. Write a python script to remove the last digit from a given number. (for example, if user enters 2534 then your output should be 253).

num1 = int(input("Enter the number: "))
#num1 = int(num1/10)
z = num1//10
print("Value: ",z)

# 2. Write a python script to get the last digit from a given number. (for example, if user enters 2089 then your output should be 9).

num2 = int(input("Enter the number: "))
d = num2%10
print("Value: ",d)

# 3. Write a python script to swap data of two variables

a=5
b=10
a,b = b,a
print("swap value: ",a,b)

# 4. Write a python script to find x power y, where values of x and y are given by user


x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
power = x**y
print("Power is: ",power)

# 5. Write a python script which takes a three digit number from the user and displays only its first digit.

num = int(input("Enter the number: "))
digit = int(num/100)
print("The first digit is: ",digit)


# 6. Write a python script which takes a three digit number from the user and displays only its middle digit.

number = int(input("Enter the number: "))
number = int(number/10)
answer = (number%10)
print(answer)

# 7. Write a python script which takes a three digit number from the user and displays only its last digit.

num3 = int(input("Enter the three digits: "))
digit2 = num3%10
print("Value: ",digit2)

# 8. Write a python script to use IN operator to display the data present in the list.

string = "i love python"
print("love" in string)

# 9. Write a python script to use NOT IN operator to display the data not present in list.

fruits = ["apple", "banana"]

print("pineapple" not in fruits)


# 10.Write a python script to use IS operator to display if both variables are the same object or not.

fruits1 = ["apple", "banana"]
fruits2 = ["apple", "banana"]
z = fruits1

print(fruits1 is z)
print(fruits1 is fruits2)
