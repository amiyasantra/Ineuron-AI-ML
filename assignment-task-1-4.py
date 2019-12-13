#  Write a Python program to find the volume of a sphere with diameter 12 cm.
#  Formula: V=4/3 * π * r3

import math                                   # import math library to get value of pi
diameter  = input("Enter diameter: ")         # taking diameter from user
if( diameter.isdigit()):                      # check for the valid input from user
    volume=4.0/3.0*math.pi*float(diameter)**3 # calculating volume a sphere with diameter
    print("volume of spleare is:", volume)    # print the value in console
else:
    print("enter valid input number!")

