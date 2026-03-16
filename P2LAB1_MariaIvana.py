#Ivana Maria 
#3/4/2026
#P2LAB1_MariaIvana
#the program will calculate the diameter, circumference, and area of a circle.
#import math module to use the constant, Math.pi
import math

#get radius from user 
radius = float(input("What is the radius of the circle? "))
print()

#cacluate diameter
diameter = 2 * radius 

#display diameter with 1 decimal point
print(f"The diameter of the circle is {diameter:.1f}\n")

#Caculate circumference
circumference = 2 * math.pi * radius 

#Display circumference with 2 decimal places 
print(f" The circumference of the circle is {circumference:.2f}\n")

#Caculate the area 
area = math.pi * radius**2 

#Display area with 3 decimal places 
print(f"The area of the circle is {area:.3f}\n")
