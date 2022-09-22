# Functions

# 1. Write a python program to create a simple function which prints “MySirG”.

def name():
    print("MySirG")
name()

# 2. Write a python program to create a function which expects two arguments and print them in the function body.

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Nishith", "Kumar")

# 3. Write a python program to create a function which expects an unknown number of arguments.

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

# 4. Write a python program to create a function which expects kwargs arguments.

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# 5. Write a python program to create a function which expects a list as an argument.

def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

print(my_function(fruits))



# 6. Write a python program to create a function that finds a maximum of four numbers.

def maximum(num1,num2,num3,num4):
    
    allNum = [num1, num2, num3, num4]
    maxNum = max(allNum)
    return maxNum


num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
num4 = int(input("Enter number 4: "))

print(maximum(num1,num2,num3,num4))

# 7. Write a python program to sum all the numbers in a list.

list1 = [11, 5, 17, 18, 23]
 
# creating sum_list function
 
 
def sumOfList(list, size):
    if (size == 0):
        return 0
    else:
        return list[size - 1] + sumOfList(list, size - 1)
 
# Driver code
total = sumOfList(list1, len(list1))
 
print("Sum of all elements in given list: ", total)

# 8. Write a python program to multiply all the numbers in a list.

def multiplyList(myList):
 
    # Multiply elements one by one
    result = 1
    for x in myList:
        result = result * x
    return result
 
 
# Driver code
list1 = [1, 2, 3]
list2 = [3, 2, 4]
print(multiplyList(list1))
print(multiplyList(list2))

# 9. Write a python program to create a function to check whether a number falls in a given range.

def test_range(n):
    if n in range(3,9):
        print( " %s is in the range"%str(n))
    else :
        print("The number is outside the given range.")
test_range(5)

# 10. Write a python program to create a function to check whether a given number is even or odd.

def even_odd(number):
    if number%2==0:
        print("even")
    else:
        print("odd")
number = int(input("Enter the number: "))
print(even_odd(number))
