# Tuple

# 1. Write a python script to store multiple items in a single variable ( Items are "Java" ,"Python", "SQL", "C" ) using tuple

mytuple = ("Java" ,"Python", "SQL", "C" )
print(mytuple)

# 2. Write a python program to store only one item using tuple.

thistuple = ("Python",)
print(type(thistuple))
print(thistuple)

# 3. Write a python program to reverse the tuple.

tuple=(1,2,3,4,5,6)
rev = tuple[::-1]
print("Reverse: ",rev)

# 4. Write a python program to Swap two tuples in Python.

tuple_1 =(10,12)
tuple_2 = (20,22)
print("Tuple before swap: ",tuple_1,tuple_2)
tuple_1,tuple_2 = tuple_2, tuple_1
print("Tuple after swap: ",tuple_1,tuple_2)

# 5. Write a python program to check if all items in the tuple are the same.

x = (40,40,40,40)
same = all(x)
print(same)

# 6. Write a python program to divide the tuple into four variables. tuple1=(100, 200, 300, 400)

tuple1=(100, 200, 300, 400)
var_1,var_2,var_3,var_4 = tuple1
print(var_1)
print(var_2)
print(var_3)
print(var_4)

# 7. Write a python program to copy elements 4 and 5 from the following tuple into a new tuple. tuple1=(1,2,3,4,5,6)

tuple1 = (1,2,3,4,5,6)
tuple2 = tuple1[3:-1]
print("Original Tuple: ",tuple1)
print("New Tuple: ",tuple2)

# 8. Write a python program to Sort a tuple of tuples by the second item. tuple1 = (('a', 21),('b', 37),('c', 11), ('d',29))

tuple1 = (('a', 21),('b', 37),('c', 11), ('d',29))
print("Orignal List: ", tuple1) 
def Sort(tuple): 
    # reverse = None (Sorts in Ascending order) 
    return(sorted(tuple1, key = lambda a: a[1]))  

print("Sorted List: ", Sort(tuple1)) 

# 9. Write a python program to print the value 20 from given nested tuple tuple1 = ("Python", [10, 20, 30], (2, 4, 16))

tuple1 = ("Python", [10, 20, 30], (2, 4, 16))
print(tuple1[1][1])

# 10. Write a python program to change the first item (22) of a list within the following tuple to 222.
# tuple1 = (11, [22, 33], 44, 55)

tuple1 = (11, [22, 33], 44, 55)
tuple1[1][0] = 222
print("Updated value",tuple1)

'''
tuple1 = (11, [22, 33], 44, 55)
list = list(tuple1)
print(list)
list[1][0]=222
tuple1 = tuple(list)
print(tuple1)
'''



