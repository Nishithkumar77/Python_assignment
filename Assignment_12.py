# 1. Write a python script to reverse a number.

n=int(input("Enter a number:"))
rev=0
while(n>0):
    a=n%10
    rev=a+rev*10
    n=n//10
print("The reverse of a number is:",rev)

# 2. Write a python script to check whether a given number is Prime or not

number = int(input('Enter number: '))

flag = 1

for i in range(2,int(number/2)):
    if number%i==0:
        flag=0
        break

if flag==1 and number>=2:
    print('Prime number')
else:
    print('Not a prime number')
    
# 3. Write a python script to print all Prime numbers under 100

import math
c=0
num=2
while(c<100):
    f=0
    for i in range(2,int(math.sqrt(num)+1)):
                   if num%i==0:
                       f=1
                       break
    if(f==0):
        print(num,end='\t')
        c=c+1
    num=num+1
print("Total Prime number = ",c)

# 4. Write a python script to print all Prime numbers between two given numbers (both values inclusive)

import math
start =int(input("Enter the starting number: "))
end =int(input("Enter the ending number: "))
count=0
for num in range(start,end):
    flag=False
    for i in range(2,int(math.sqrt(num)+1)):
                   if num%i==0:
                       flag=True
                       break
    if(flag==False and num>=2):
        print(num,end='\t')
        count=count+1
print("Total Prime number = ",count)

# 5. Write a python script to find next prime number of a given number.

n = int(input("Enter a number: "))

while True:
    n+=1
    for  x in range(2,n):
        if n%x==0:
           break
    else:
         print("next prime number is",n)
         break

# 6. Write a python script to print first N prime numbers

import math
number = int(input("Enter the number: "))
c=0
num=2
while(c<number):
    f=0
    for i in range(2,int(math.sqrt(num)+1)):
                   if num%i==0:
                       f=1
                       break
    if(f==0):
        print(num,end='\t')
        c=c+1
    num=num+1
print("Total Prime number = ",c)

# 7. Write a python script to check whether a given pair of numbers are co-Prime numbers or not.

num1= int(input("Enter the first number: "))
num2= int(input("Enter the second number: "))

mn = min(num1, num2)

for i in range(1, mn+1):

    if num1%i==0 and num2%i==0:
        hcf = i
    
if hcf == 1:
    print("Yes! They are Co-Prime.")

else:
    print("Sorry! They are not Co-Prime.")
    
# 8. Write a python script to print first N terms of a Fibonacci series

nterm = int(input("Enter how many terms?: "))
# first two terms
n1,n2=0,1
count=0
if nterm<=0:
    print("Enter a positive number")
elif nterm==1:
    print("Fibonacci sequence upto",nterm,":")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count<nterm:
        print(n1)
        nth=n1+n2
        n1,n2=n2,nth  # updated values
        count+=1

# 9. Write a python script to calculate LCM of two numbers

num_1 =int(input("Enter the first number: "))
num_2 =int(input("Enter the second number: "))
if (num_1<num_2):
    c=num_1
else:
    c=num_2
for i in range(c,0,-1):
    if (num_1%i==0 and num_2%i==0):
        break
print("LCM = ",(num_1*num_2)//i)
    
# 10. Write a python script to calculate HCF of two numbers

num_1 =int(input("Enter the first number: "))
num_2 =int(input("Enter the second number: "))
if (num_1<num_2):
    c=num_1
else:
    c=num_2
for i in range(c,0,-1):
    if (num_1%i==0 and num_2%i==0):
        break
print("HCF = ",i)
