#!/usr/bin/env python
# coding: utf-8

# Create a dog object that will inherit all the variables and methods of the parent class Animal 
# 
# and display it.

# In[3]:


class Animal:
    def __init__(self, name , color):
        self.name = name
        self.color = color
    def animal_name_and_color(self):
        print("The dog name is {} and his color is {}.".format(self.name, self.color))

dog = Animal("Dior" , "black")
dog.animal_name_and_color()


# Demonstrate the working of Polymorphism by creating two classes -Car and Bike. 
# 
# 
# Display the information like name, color, and number of wheels

# In[27]:


class Car:
    def __init__(self, name , color , wheels):
        self.name = name
        self.color = color
        self.wheels = wheels
    def information(self):
        print("Car information: {} , {} , {} wheels.".format(self.name, self.color , self.wheels))
        
class Bike:
    def __init__(self, name , color , wheels):
        self.name = name
        self.color = color
        self.wheels = wheels
    def information(self):
        print("Bike information: {} , {} , {} wheels.".format(self.name, self.color , self.wheels))

car = Car("Toyota" , "Blue" , 4)
car.information()
bike =Bike('LX' , 'Gray', 2)
bike.information()


# Create a list of tuples containing the 5 planets of our solar system along with their moons as-earth
# 
# having 1 moon, Jupiter having 79 moons, Saturn having 82 moons, Uranus having 27 moons and Neptune
# 
# having 14 moons.Sort the list according to the ascending number of moons along with the names of
# 
# planet using Lambda function. Display both original and sorted list.

# In[12]:


list_of_planets = [("Earth", 1) , ("Jupiter" , 79) , ("Saturn" , 82) , ("Uranus", 27) , ("Neptune", 14)]
sorted(list_of_planets,key = lambda x:x[1])


# Create two functions -fillup and use, which uses a global variable as tank. Use the global variable in
# 
# both the functions to return the quantity of fuel present in the tank after filling up the tank and
# 
# after using the fuel of the tank. Show the working of two functions only. It is not necessary to
# 
# display the outputs.

# In[15]:


tank = 0
def  fillup():
    global tank 
    tank = 10
    print("Tank is fill up at {}.".format(tank))
    
def use():
    global tank 
    tank = 5
    print("Tank is used at {}.".format(tank))
    
fillup()
use()


# Write a program to depict the use of multiple inheritance. The program should contain 4 classes -class
# 
# 4 should inherit from class 2 and class 3. Similarly, class 2 should inherit from class 1. Class 3 
# 
# should inherit from class 1. Each class should have its own print statement

# In[16]:


class Class_1:
    def __init(self, name):
        self.name = name
    def class_name(self):
        print("Class number is {}.".format(self.name))
        
class Class_2(Class_1):
    def __init(self, color):
        self.color = color
    def class_color(self):
        print("Class number is {}.".format(self.color))
        
class Class_3(Class_1):
    def __init(self, height):
        self.height = heigt
    def class_height(self):
        print("Class number is {}.".format(self.height))
        
class Class_4(Class_2 ,Class_3):
    def __init(self, location):
        self.location = location
    def class_location(self):
        print("Class number is {}.".format(self.location))
     
     


# Use Getter and Setter method to set the name and age of a person. Moreover, get the name and age of
# 
# 
# the same person

# In[26]:


class Getter_Setter:
    def _init_(name, age):
        self.name = name
        self.age = age
    def setter(self):
        self.name = input("Enter your name:")
        self.age = int(input("Enter your age:"))
        return self.name, self.age
    def getter(self):
        print("My name is {} and I am {} years old.".format( self.name , self.age))
obj =Getter_Setter()
obj.setter()
obj.getter()


# In[ ]:





# In[ ]:




