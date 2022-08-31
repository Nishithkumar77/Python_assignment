# 1. Write a Python script to create a list of first N natural numbers.

l=[]
n=int(input("Enter size of list "))
for i in range(0,n):
    e=int(input("Enter element of list "))
    l.append(e)
print("Original list: ",l)

# 2. Write a Python script to create a list of first N odd natural numbers.

l=[]
n=int(input("Enter size of list "))
for i in range(0,n):
    e=int(input("Enter element of list "))
    if e%2!=0:
        l.append(e)
print("Original list of odd natural numner: ",l)

# 3. Write a Python script to create a list of first N even natural numbers.

l=[]
n=int(input("Enter size of list "))
for i in range(0,n):
    e=int(input("Enter element of list "))
    if e%2==0:
        l.append(e)
print("Original list of even natural numner: ",l)

# 4. Write a Python script to find the greatest number in a given list of numbers.

list = [44,10,50,12,60,36]
print(max(list))    # max is used to find greatest value in th list

# 5. Write a Python script to find the smallest number in a given list of numbers.

list = [44,10,50,12,60,36]
print(min(list))    # min is used to find smaller value in th list

# 6. Write a Python script to calculate the sum of elements in a given list of numbers.

list = [44,10,50,12,60,36]
print(sum(list))    # sum is used to find sum of all value in th list

# 7. Write a Python script to remove all non int values from a list.

list = [44,10,50,12,60,"Rahul"]
list.remove("Rahul")    # remove is used to delete any value in th list
print(list)

# 8. Write a Python script to print distinct elements along with their frequencies of occurrence in the list.

l=[]
n=int(input("Enter size of list "))
for i in range(0,n):
    e=int(input("Enter element of list "))
    l.append(e)
print("Original list: ",l)

n=int(input("Enter element to be checked list: "))
print(n," has occurred ",l.count(n),"times")

# 9. Write a Python script to print indices of all occurrences of a given element in a given list.

list = [1, 2, 3, 1, 5, 4]
list_size = len(list) 
 
# declare for loop
for i in range(list_size): 
   
      # check the condition
    if(list[i] == 1): 
       
          # print the indices
        print(i) 

# 10. Write a python script to sort a list.

l=[]
n=int(input("Enter size of list "))
for i in range(0,n):
    e=int(input("Enter element of list "))
    l.append(e)
print("Original list: ",l)
l.sort()  # used to sort the list
print("List after sorting: ",l)
