# 1. Write a python script to print MySirG N times on the screen

i=1
n = int(input("Enter How many times you want to print: "))
while i<=n:
    print("MySirG")
    i+=1


# 2. Write a python script to print first N natural numbers

i=1
n = int(input("Enter How many natural number you want to print: "))
while i<=n:
    print(i,sep=' ')
    i+=1
    
# 3. Write a python script to print first N natural numbers in reverse order

i=1
n = int(input("Enter How many natural number you want to print into reverse: "))
while i<=n:
    print(n-i,end=' ')
    i+=1


# 4. Write a python script to print first N odd natural numbers

i=1
n = int(input("Enter How many odd natural number you want to print: "))
while i<=n:
    if i%2!=0:
        print(i,end=' ')
    i+=1

# 5. Write a python script to print first N odd natural numbers in reverse order

i=1
n = int(input("Enter How many odd natural number you want to print in reverse order: "))
while i<=n:
    if i%2!=0:
        print(n-i,end=' ')
    i+=1

# 6. Write a python script to print first N even natural numbers

i=1
n = int(input("Enter How many even natural number you want to print: "))
while i<=n:
    if i%2==0:
        print(i,end=' ')
    i+=1

# 7. Write a python script to print first N even natural numbers in reverse order

i=1
n = int(input("Enter How many even natural number you want to print in reverse order: "))
while i<=n:
    if i%2==0:
        print(i,end=' ')
    i-=1
    
# 8. Write a python script to print squares of first N natural numbers

i=1
n = int(input("Enter the number: "))
while i<=n:
        print(i**2,end=' ')
        i+=1

# 9. Write a python script to print cubes of first N natural numbers

i=1
n = int(input("Enter the number: "))
while i<=n:
        print(i**3,end=' ')
        i+=1

# 10. Write a python script to print first 10 multiples of N

i=1
n = int(input("Enter the number: "))
while i<=10:
        print(i*n,end=' ')
        i+=1

