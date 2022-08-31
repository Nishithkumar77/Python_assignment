# Set

# 1. Write a python program to store all the programming languages known to you using Set.

language = input("Enter your programming language separated by comma: ")
program = {eval(e) for e in language.split(',')}
print(program)

# 2. Write a python program to store your own information {name, age, gender, so on..}

info = input("Enter your personal details separated by comma: ")
info_s = {eval(e) for e in info.split(',')}
print(info_s)

# 3. Write a python script to get the data type of a Set.

s ={2,10,5,8,7,6,4}
s = set(s)
print(type(s))

# 4. Write a Python script to find if “Python” is present in the set thisset = {"Java", "Python", "Django"}

thisset = {"Java", "Python", "Django"}
str = input("Enter string you want to find in thisset: ")
if str in thisset:
    print(str,"present in thisset")
else:
    print(str,"not present in thisset")
    
# 5. Write a python program to add items from another set to the current set. thisset = {"Java", "Python", "SQL"} secondset= {"C", "Cpp", "NoSQL"}

thisset = {"Java", "Python", "SQL"}
secondset= {"C", "Cpp", "NoSQL"}
thisset.update(secondset)
print(thisset)

# 6. Write a python program to add elements of list to a set
# thisset = {"Python", "Django", "JavaScript"}
# mylist = ["Java", "C"]

thisset = {"Python", "Django", "JavaScript"}
mylist = ["Java", "C"]
thisset.update(mylist)
print(thisset)

# 7. Write a python program to remove last item of the given set thisset = {"Python", "Django", "JavaScript", "SQL"}

thisset = {"Python", "Django", "JavaScript", "SQL"}
thisset.discard("SQL")
print(thisset)

# 8. Write a python program to delete the set completely.

thisset = {"Python", "Django", "JavaScript", "SQL"}
thisset.clear()
print(thisset)


# 9. Write a python program to loop through the set and print values
# thisset = {"Python", "Django", "JavaScript", "SQL"}

thisset = {"Python", "Django", "JavaScript", "SQL"}
for ele in thisset:
    print(ele)

# 10. Write a python program to find the maximum and minimum value in a set.

s ={2,10,5,8,7,6,4}
print("Maxium value is: ",max(s))
print("Minimum Value is: ",min(s))
