# 1. Write a python script to calculate sum of first N natural numbers

num = int(input("Enter the number: "))
sum=0
while(num>0):
    sum=sum+num
    num-=1
    print("The sum of first n natural number is",sum)
    
# 2. Write a python script to calculate sum of squares of first N natural numbers

num = int(input("Enter the number: "))
sum=0
for i in range(1,num+1):
    s=i**2
    sum+=s
    print("The sum is:",sum)
    
# 3. Write a python script to calculate sum of cubes of first N natural numbers

num = int(input("Enter the number: "))
sum=0
for i in range(1,num+1):
    cube=i**3
    sum+=cube
    print("The sum is:",sum)
    
# 4. Write a python script to calculate sum of first N odd natural numbers

# Take input from user.
num = int(input("Print sum of odd numbers till : "))
sum = 0

for i in range(1, num + 1):

    #Check for odd or not.
    if((i % 2)!= 0):
        sum += i

print("\nSum of odd numbers from 1 to", num, "is :", sum)


# 5. Write a python script to calculate sum of first N even natural numbers

# Take input from user.
num = int(input("Print sum of even numbers till : "))
sum = 0

for i in range(1, num + 1):

    #Check for odd or not.
    if((i % 2)== 0):
        sum += i

print("\nSum of even numbers from 1 to", num, "is :", sum)

# 6. Write a python script to calculate factorial of a given number

number = int(input('Enter Number: '))
factorial = 1
for i in range(1, number+1):
    factorial = factorial*i

# Displaying factorial value
print('Factorial of %d is %d' %(number, factorial))



# 7. Write a python script to count digits in a given number

num = int(input("Enter a number: "))
count=0
while (num>0):
        count+=1
        num=num//10
        print("count digit",count)

# 8. Write a python script to calculate sum of digits of a given number

n=int(input("Enter a number:"))
sum=0
while(n>0):
    a=n%10
    sum=sum+a
    n=n//10
print("The total sum of digits is:",sum)

# 9. Write a python script to print binary equivalent of a given decimal number. (do not use bin() method)

n=int(input("Enter a number: "))
a=[]
while(n>0):
    dig=n%2
    a.append(dig)
    n=n//2
a.reverse()
print("Binary Equivalent is: ")
for i in a:
    print(i,end=" ")
    
# 10. Write a python script to print the octal equivalent of a given decimal number. (do not use oct() method)

print("Enter the Decimal Number: ")
decnum = int(input())

i = 0
octnum = []
while decnum!=0:
    rem = decnum%8
    octnum.insert(i, rem)
    i = i+1
    decnum = int(decnum/8)

print("\nEquivalent Octal Value is: ")
i = i-1
while i>=0:
    print(octnum[i], end="")
    i = i-1
print()
