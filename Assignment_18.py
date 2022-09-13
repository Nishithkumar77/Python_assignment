# Dictionary
# 1. Write a python program to create and print a dictionary which stores your information. (name, age, gender …..)
details = {}
key = input("Enter Name: ")
data = int(input("Enter Age: "))
data1 = input("Enter Gender: ")
details[key] = data,data1
print(details)
# 2. Write a python program to access the items of a dictionary by referring to its key name.

sample_dict = {'C': 92,'Java': 66,'Python': 85}
print(key[Java])

# 3. Write a python program to get a list of the values from a dictionary.

data = {'manoja': 'java', 'tripura': 'python',
        'manoj': 'statistics', 'manoji': 'cpp'}
 
# get list of values
list(data.values())
    
# 4. Write a python program to change the value of a specific item by referring to its key name.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

# 5. Write a python program to print all key names in the dictionary, one by one.
sample_dict = {
'C': 92,
'Java': 66,
'Python': 85
}
for i in sample_dict:
    print(i)
# 6. Write a python program to create a dictionary that contains three dictionaries. (nested)

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

# 7. Write a python program to create three dictionaries, then create one dictionary that will contain the other three dictionaries.

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

# 8. Write a python program to convert two lists into a dictionary in a way that item from list1 is the key and item from list2 is the value.

test_keys = ["Rash", "Kil", "Varsha"]
test_values = [1, 4, 5]
print ("Original key list is : " + str(test_keys))
print ("Original value list is : " + str(test_values))
  
res = {test_keys[i]: test_values[i] for i in range(len(test_keys))}
  
print ("Resultant dictionary is : " +  str(res))

# 9. Write a python program to merge two python dictionaries into one dictionary.

dict_1 = {1: 'a', 2: 'b'}
dict_2 = {2: 'c', 4: 'd'}

dict_3 = dict_2.copy()
dict_3.update(dict_1)

print(dict_3)

# 10. Write a python program to get the key of lowest value from the dictionary.
'''
sample_dict = {
'C': 92,
'Java': 66,
'Python': 85
}
'''

sample_dict = {'C': 92,'Java': 66,'Python': 85}
print(min(sample_dict))
