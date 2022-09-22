# More on Recursion

# 1. Write a recursive python function to calculate sum of first N natural numbers

def sum(n):
    if n <= 1:
       return n
    else:
       return n + sum(n-1)
num = int(input("Enter the number: "))

if num < 0:
   print("Enter a positive number")
else:
   print("The sum is",sum(num))
    
# 2. Write a recursive python function to calculate sum of first N odd natural numbers

def OddSum(n):
    if n>0:
        x=(n*2)-1
        return x + OddSum(n-1)
    else:
        return 0

n = int(input("Enter the number: "))
print(OddSum(n))

# 3. Write a recursive python function to calculate sum of first N even natural numbers

def sum_of_even(n):
    sum1 = 0
    if n == 0:
        return sum1

    elif n % 2 == 0:
        sum1 += n
    
    return sum1 + sum_of_even(n - 1)

n = int(input("Enter the number: "))
print(sum_of_even(n))

# 4. Write a recursive python function to calculate sum of squares of first N natural numbers

def squaresum(n) :
    sm = 0
    for i in range(1, n+1) :
        sm = sm + (i * i)
      
    return sm
n = int(input("Enter the number: "))
print(squaresum(n))


# 5. Write a recursive python function to calculate sum of cubes of first N natural numbers

def cubesum(n) :
    sm = 0
    for i in range(1, n+1) :
        sm = sm + (i*i*i)
      
    return sm
n = int(input("Enter the number: "))
print(cubesum(n))

# 6. Write a recursive python function to calculate the factorial of a number.

def fact(n):
    if n == 1:
        return n
    else:
        return n * fact(n - 1)

n = int(input("Enter the number: "))
print(fact(n))

# 7. Write a recursive python function to calculate sum of the digits of a given number

def sum_of_digit(n):
    if n == 0:
        return 0
    return (n % 10 + sum_of_digit(int(n / 10)))
 
# Driven code to check above
num = int(input("Enter the number: "))
result = sum_of_digit(num)
print("Sum of digits in",num,"is", result)

# 8. Write a recursive python function to print binary of a given decimal number.

def find(decimal_number):
    if decimal_number == 0:
        return 0
    else:
        return (decimal_number % 2 + 10 * find(int(decimal_number // 2)))
 
# Driver Code
decimal_number = int(input("Enter the number: "))
print(find(decimal_number))

# 9. Write a recursive python function to print octal of a given decimal number

def Octal(n):
    octal = oct(n)
    return octal
# Driver Code
n = int(input("Enter the number: "))
print(Octal(n))

# 10. Write a recursive python function to find the Nth term of the Fibonacci series.

def recursive_fibonacci(n):
  if n <= 1:
      return n
  else:
      return(recursive_fibonacci(n-1) + recursive_fibonacci(n-2))
 
n_terms = int(input("Enter the nth term: "))
 
# check if the number of terms is valid
if n_terms <= 0:
  print("Invalid input ! Please input a positive value")
else:
  print("Fibonacci series:")
for i in range(n_terms):
    print(recursive_fibonacci(i),end=" ")
