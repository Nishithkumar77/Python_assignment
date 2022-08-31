# 1. Write a python script to store multiple items in a single variable ( Items are “Java”,“Python”, “SQL”, “C” ) using list.

a="Java"
b="Python"
c="SQL"
d="C"
l1 = [a,b,c,d]
print(l1)

#2. Write a python script to get the data type of a list.

list = ["Java", "C", "Python"]
print(type(list))

#3. Write a python script to get the last item of the list ( mylist = ["Java", "C", "Python"])

mylist = ["Java", "C", "Python"]
print(mylist[-1])  ## fetching last item

#4. Write a python script to Change the values "SQL" and "Reactnative" with the values
#"NoSQL" and "Flutter" (List is thislist = ["Java", "SQL", "C", "Reactnative","Javascript", "Python"]

thislist = ["Java", "SQL", "C", "Reactnative","Javascript", "Python"]
thislist[1]="NOSQL"
thislist[3]="Flutter"
print(thislist)

# 5. Write a python script to add an item to the end of the list (item “Python”. (mylist = ["Java", "SQL", "C", "Reactnative"])

mylist = ["Java", "SQL", "C", "Reactnative"]
mylist.append("Python")
print(mylist)

# 6. Write a python program to append elements from another list to the current list.

firstlist = ["Java", "Python", "SQL"]
secondlist = ["C", "Cpp", "NoSQL"]
newlist = firstlist + secondlist
print(newlist)

# 7. Write a python program to Print all items by referring to their index number.

thislist = ["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]
for index in range(len(thislist)):
    value = thislist[index]
    print(index, value)

# 8. Write a python program to sort the list alphanumerically – thislist = ["Java", "SQL", "C", "Reactjs", "Javascript", "Python"]

thislist = ["Java", "SQL","C", "Reactjs", "Javascript", "Python"]
thislist.sort()
print(thislist)

# 9. Write a Python script to create a list of city names taken from the user.

print("Enter city names: ")
l1=eval(input())
print(l1)

# 10. Write a Python script to create a list, where each element of the list is a digit of a given number.

# initializing list
#test_list = [56, 72, 875, 9, 173]
l=[]
n=int(input("Enter size of list "))
for i in range(0,n):
    e=int(input("Enter element of list "))
    l.append(e)
print("Original list: " +str(l))

# initializing K
K = int(input("Enter the number: "))

# extracting all elements with digit K using
# in operator after string conversion using str()
res = [ele for ele in l if str(K) in str(ele)]

# printing result
print("Elements with digit K : " + str(res))
