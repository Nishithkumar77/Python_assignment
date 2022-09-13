# Recursion

# 1. Write a recursive python function to print first N natural numbers.

def printNumber(n):
  if n > 0:
    printNumber(n - 1)
    print(n, end = ' ')

n = 10
printNumber(n)

        
# 2. Write a recursive python function to print first N natural numbers in reverse order

def PrintReverseOrder(N):
    
    if (N <= 0):
        return;
    else:
        print(N, end = ' ')
        PrintReverseOrder(N - 1)
         
N = int(input("Enter the number: "))
PrintReverseOrder(N)

# 3. Write a recursive python function to print first N odd natural numbers

def odd(i,count=1):
    if (count<=1):
        print(2*count-1)
        odd(n,count+1)
odd(10)

# 4. Write a recursive python function to print first N odd natural numbers in reverse order.


# 5. Write a recursive python function to print first N even natural numbers.

def printeven(i,N):
    if(i<=N):
        print(2*i, end=' ')
        printeven(i+1,N) # recursive call 
printeven(1,10)

# 6. Write a recursive python function to print first N even natural numbers in reverse order.

def EvenReverse(n):
  if n>0:
    print(2*n,end=' ')
    EvenReverse(n-1)

n = int(input("Enter the number: "))
print(EvenReverse(n))
  
# 7. Write a recursive python function to print squares of first N natural numbers



# 8. Write a recursive python function to print cubes of first N natural numbers
# 9. Write a recursive python function to print first N multiples of a given number.

def multiple(m, n):
  
    a = range(n, (m * n)+1, n)
      
    print(*a)
  
m = int(input("Enter number of multiple you want"))
n = int(input("Enter the number"))
multiple(m, n)

# 10. Write a recursive python function to print a number in reverse order.
