#Ivana Maria
#3/16/2026
#P3LAB_MariaIvana
#This program allows the user to enter a money (float) value with two places after the decimal.

#Get value from user
Change = float(input("Enter an amount of money: $"))
print(f"Change Amount: {Change}")

#converting the value to an integar
Change = round(Change * 100)

#determine how many dollars are needed
num_dollars = Change // 100 
Change = Change - (num_dollars * 100)

num_quarters = Change // 25 
Change = Change - (num_quarters * 25) 

num_dimes = Change // 10 
Change = Change - (num_dimes * 10)

num_nickels = Change // 5 
Change = Change - (num_nickels * 5)

num_pennies = Change

if num_dollars > 0:
    if num_dollars == 1: 
      print(f"{num_dollars} Dollar")
    else: 
       print(f"{num_dollars} Dollars")

if num_quarters > 0:
   if num_quarters == 1:
      print(f"{num_quarters} Quarter")
   else:
      print(f"{num_quarters} Quarters")

if num_dimes > 0:
   if num_dimes == 1:
      print(f"{num_dimes} Dime")
   else:
      print(f"{num_dimes} Dimes")

if num_nickels > 0: 
   if num_nickels == 1: 
      print(f"{num_nickels} Nickel")
   else:
      print(f"{num_nickels} Nickels")

if num_pennies > 0: 
   if num_pennies == 1:
      print(f"{num_pennies} Penny")
   else:
      print(f"{num_pennies} Pennies")

