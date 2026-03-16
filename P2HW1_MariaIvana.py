#Ivana Maria 
#3/10/2026
#P2HW1_MariaIvana
# This program calculates and display travel expense

print(f"This program calculates and display travel expense.")

Budget = float(input("Enter Budget: "))
destination= input("Enter your travel destination: ")
fuel = float(input("How much do you think you will spend on gas? "))
hotel = float(input("Approximately how much will you need for accommondation/hotel? "))
food = float(input("Last, how much do you need for food? "))

remaining = Budget - (fuel + hotel + food)

print("---------Travel Expense--------")

print(f"{"Location:":15s}{"New York City":5s}")

print(f"{"Initial Budget:":<15s} ${2000:.2f}")

print(f"{"Fuel:":<15s} ${450:.2f}") 

print(f"{"Accomodation:":<15s} ${600:.2f}")

print(f"{"Food:":<15s} ${250:.2f}")

print("---------------------------------")

print(f"{"Remaining Balance:":<15s} ${700:.2f}")