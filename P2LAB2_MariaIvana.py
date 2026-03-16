#Ivana Maria
#3/7/2026
#P2LAB2_MariaIvana
#Write a program that creates a dictionary where the key and value pairs are as follows

cars = {'Camaro': 18.21, 'Prius': 52.36, 'Models S': 110,'Silverado': 26}

#Keys from the dictionary 
cars_keys = cars.keys()

print(cars_keys)

#Get a car from user 
car_name = input("Enter a car: ")

#Get mpg for the car 
car_mpg = cars[car_name]
print(f"The {car_name} gets {car_mpg} miles per gallon.")

#Get miles from car
miles = float(input(f" How many miles will you drive the {car_name}? "))

#caculate 
gallons = miles / car_mpg 

#Display results 
print(f"{gallons:.2f} gallons of gas are needed to drive the {car_name} {miles} miles.")