#Ivana Maria 
#3/1/26 
#P1HW2_MariaIvana
#Travel expense summary 


print("This Program caculates and display travel expenses")

budget = float(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
gas = float(input("How much do you think you spend on gas? "))
accommondation =float(input ("Approximately, how much will you need for accommondation/hotel? "))
food = float(input("Last, how much do you need for food? "))

total_expense = gas + accommondation + food 
remaining_balance = budget - total_expense

print("\n----Travel Expenses----")
print(f"location: {destination}")
print(f"Initial Budget: {budget:.2f}\n")

print(f"fuel: {gas:.2f}")
print(f"accommondation: {accommondation: .2f}")
print(f"food: {food: .2f}\n")

print(f"remaining balance: {remaining_balance: .2f}")
