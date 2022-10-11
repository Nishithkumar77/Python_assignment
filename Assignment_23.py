# Iterator, Generator and Decorator

# 1. Use iter and next method to access all the elements of a given set using while loop

set = {1,2,3,4,5,6,7,8}
it=iter(set)
while True:
    try:
        # get the next item
        element = next(it)
        print(element, end=' ')
        # do something with element
    except StopIteration:
        # if StopIteration is raised, break from loop
        break

# 2. Create a generator to produce first n odd natural numbers

def odd(n):
    a=1
    while n:
        yield a
        a+=2
        n-=1
for i in odd(int(input("Enter the number: "))):
    print(i,end=' ')
    
# 3. Create a generator to produce first n even natural numbers

def even(n):
    a=2
    while n:
        yield a
        a+=2
        n-=1
for i in even(int(input("Enter the number: "))):
    print(i,end=' ')

# 4. Create a generator to produce squares of first N natural numbers.

def square(n):
    a=1
    while n:
        yield a
        a+=1
        n-=1
for i in square(int(input("Enter the number: "))):
    print(i**2,end=' ')


# 5. Create a generator to produce first n terms of Fibonacci series

def fib(n):
    a,b=0,1
    while n:
        yield a
        a,b=b,a+b
        n-=1
for f in fib(int(input("Enter the number: "))):
    print(f,end=' ')
    
# 6. Create a generator to produce first n prime numbers
def isPrime(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True

def prime(n):
    num=2
    while n:
        if isPrime(num):
            yield num
            n-=1
        num+=1
    return
it = prime(10)
for e in it:
    print(e,end=' ')

# 7. Create an endless iterator using generator method to produce terms of Fibonacci series

li = [f for f in fib(int(input("Enter the number: ")))]
print(li)

# 8. Create an endless iterator using generator method to produce Prime numbers
# 9. Define a function which takes lengths of three sides of a triangle as arguments and display the perimeter or triangle. Define and apply a decorator which checks for the
# validity of the triangle on the basis of lengths of the side. This makes the perimeter to be displayed when the triangle can exist with the given lengths of the sides.
# 10. Define a function which calculates HCF of two numbers. Define and apply a decorator to check whether two given numbers are co-prime or not.
