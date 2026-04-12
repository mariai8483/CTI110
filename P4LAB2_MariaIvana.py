#Ivana Maria
#4/3/2026
#P4LAB2_MariaIvana.py
#use while loop and for loop together

run_again = 'yes'

while run_again != "no":

#get value integar from user 
 user_num = int(input("Enter an integer: "))

 if user_num >= 0:
    #display multiplication for that value and range (1-12)
    for item in range(1, 13):
        print(f"{user_num} * {item} = {user_num * item}")
 else:
    print("This program does not handle negative values")
 run_again = input("Would you like to run the program again? ")

#loop has broken. user entered "no"
print("Program is ending....")
