'''
Write a Python Program(with class concepts) to find the area of the triangle using the below

formula.

area = (s*(s-a)*(s-b)*(s-c)) ** 0.5

Function to take the length of the sides of triangle from user should be defined in the parent

class and function to calculate the area should be defined in subclass.
'''

###################(user define parent class)##################
class Triangle_parent:                       # Define Triangle_parent class  
    def __init__(self, side1, side2, side3): # useing a predefine __init__ method to get and store side value of tringle
        self.side1 = side1                  
        self.side2 = side2
        self.side3 = side3
        print ("Initialised Triagle parent class by [" +  str(side1) + "," + str(side2) + "," + str(side3) + "]")

##################(user define child class)###################

class Triangle_Inherit(Triangle_parent):     # Define Triangle_Inherit class with inherite property of Triangle_parent class
 
 def __init__(self, side1, side2, side3):    # useing a predefine __init__ method to get and store side value of tringle
        print ("Initialised inherite property of parent class" )
        super(Triangle_Inherit, self).__init__(side1, side2, side3) # Initialised inherite property of parent class using super class
        
 def area(self):                             # define a area methode to claulate tingle area
    s = (self.side1 + self.side2 + self.side3)/2 # calculating half perimeter 
    return (s*(s-self.side1)*(s-self.side2)*(s-self.side3))**0.5    # return area of triangle using herons formula

##################(Main Methode)##############################

Triangle = Triangle_Inherit(5,5,5)                    # define a Triangle object  
print ("Area of triangle = " + str(Triangle.area()) ) # printing the area of triangle
