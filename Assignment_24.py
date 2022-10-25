# Classes and Objects
# 1. Write a python program to create a user class with 3 properties : name, age, email.

class mydata:
    def __init__(self,name,age,email):
        self.name= name
        self.age= age
        self.email= email
    def display(self):
        print('Name:',self.name)
        print('Age:',self.age)
        print('E-mail:',self.email)
s = mydata("Nishith Kumar",27,"nsahani99@gmail.com")
s.display()

# 2. Write a python program to create a user class with a method to greet the user.

class Person:
    age = 10

    def greet(self):
        print('Hello')
harry = Person()
print(Person.greet)
print(harry.greet)
harry.greet()

# 3. Write a python program to create 2 objects of the user class and assign different values.

class Dog:
 
    # Class Variable
    animal = 'dog'
 
    # The init method or constructor
    def __init__(self, breed, color):
 
        # Instance Variable
        self.breed = breed
        self.color = color
 
 
# Objects of Dog class
Rodger = Dog("Pug", "brown")
Buzo = Dog("Bulldog", "black")
 
print('Rodger details:')
print('Rodger is a', Rodger.animal)
print('Breed: ', Rodger.breed)
print('Color: ', Rodger.color)
 
print('\nBuzo details:')
print('Buzo is a', Buzo.animal)
print('Breed: ', Buzo.breed)
print('Color: ', Buzo.color)
 
# Class variables can be accessed using class
# name also
print("\nAccessing class variable using class name")
print(Dog.animal)

# 4. Write a python program to init default values for user object using __init__ method.

class Person:
 
    # init method or constructor
    def __init__(self, name):
        self.name = name
 
    # Sample Method
    def say_hi(self):
        print('Hello, my name is', self.name)
 
 
# Creating different objects
p1 = Person('Nikhil')
p2 = Person('Abhinav')
p3 = Person('Anshul')
 
p1.say_hi()
p2.say_hi()
p3.say_hi()

# 5. Write a python program to delete the age property of the user.

class mydata:
    def __init__(self,name,age,email):
        self.name= name
        self.age= age
        self.email= email
    def display(self):
        print('Name:',self.name)
        print('Age:',self.age)
        print('E-mail:',self.email)
s = mydata("Nishith Kumar",27,"nsahani99@gmail.com")
s.display()
del s.age

# 6. Write a python program to create 3 user objects and find the youngest of all.
# 7. Write a python program to create a Laptop class with 4 attributes (brand, ram, cpu, hdd) and 2 methods (showConfig() to print the values, __init__() to initialize the values).

class laptop:
    def __init__(self,brand,ram,cpu,hdd):
        self.brand = brand
        self.ram = ram
        self.cpu = cpu
        self.hdd = hdd
    def showconfig(self):
        print("Brand",self.brand)
        print("RAM",self.ram)
        print("CPU",self.cpu)
        print("HDD",self.hdd)
show = laptop("HP","32GB","I3","1TB")
show.showconfig()

# 8. WRT 7th Question, create 3 Laptop objects and add them to the list in the sorted order based on the ram size.

class laptop:
 
    def __init__(self,brand,ram,cpu,hdd):
        self.brand = brand
        self.ram = ram
        self.cpu = cpu
        self.hdd = hdd
    def __repr__(self):
        return str((self.brand, self.ram, self.cpu, self.hdd))
    
laptop = [
    laptop("HP",32,"I9","1TB"),
    laptop("DELL",12,"I7","1TB"),
    laptop("LENOVO",8,"I5","1TB")
    ]
 
print(sorted(laptop, key=lambda x: x.ram))

# 9. Write a python program to create a School class and 3 instance variables and 1 class variable.


# 10. Define a class Employee with instance object variables empid, name, salary. Write __init__() method in the class to initialize instance object variables. Also define
# instance methods to input fields and display field values

class Employee:
    def __init__(self,eid,ename,esal):
        self.eid=eid
        self.ename=ename
        self.esal=esal
    def display(self):
        print('Employee ID:',self.eid)
        print('Employee Name:',self.ename)
        print('Employee Salary:',self.esal)

e=Employee(100,'Nishith',10000)
e.display()


