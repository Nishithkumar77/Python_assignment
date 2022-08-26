# 1. Write a python script to print MySirG N times on the screen

n = int(input("Enter how many times you want to print: "))
for i in range(n):
        print("MySirG",end=' ')
        i+=1
        
# 2. Write a python script to print first N natural numbers

num = int(input("Enter how many natural number you want to print: "))
for i in range(num):
        print(i+1,end=' ')
        
# 3. Write a python script to print first N natural numbers in reverse order

num_rev = int(input("Enter how many natural number you want to print: "))
for i in range(num_rev):
        print(num_rev-i,end=' ')
        i+=1

# 4. Write a python script to print first N odd natural numbers

num_odd = int(input("Enter how many odd number you want to print: "))
for i in range(num_odd):
    if i%2!=0:
        print(i,end=' ')
    i+=1
    
# 5. Write a python script to print first N odd natural numbers in reverse order

num_odd_rev = int(input("Enter how many odd number you want to print i reverse: "))
for i in range(num_odd_rev):
    if i%2!=0:
        print(num_odd_rev-i,end=' ')
    i+=1
# 6. Write a python script to print first N even natural numbers

num_even = int(input("Enter how many even number you want to print: "))
for i in range(2,num_even,2):
        print(i,end=' ')
        
# 7. Write a python script to print first N even natural numbers in reverse order

for a in range(2*int(input("Enter a number")),0,-2):
    print(a,end=' ')

    
# 8. Write a python script to print squares of first N natural numbers

num_square = int(input("Enter the number: "))
for i in range(num_square):
        print((i+1)**2,end=' ')

# 9. Write a python script to print cubes of first N natural numbers

num_cube = int(input("Enter the number: "))
for i in range(num_cube):
        print((i+1)**3,end=' ')

# 10. Write a python script to print first 10 multiples of N

num_mul = int(input("Enter the number: "))
for i in range(1,num_mul+1):
        print(i*num_mul,end=' ')
