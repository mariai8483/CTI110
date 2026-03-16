#Ivana Maria 
#3/15/2026
#P2HW2_MariaIvana
#This program caculates grades from lowest to hightest and sum it up. 

#Enter grades for module 1-6

Module1 = float(input("Enter grade for Module 1: "))
Module2 = float(input("Enter grade for Module 2: "))
Module3 = float(input("Enter grade for Module 3: "))
Module4 = float(input("Enter grade for Module 4: "))
Module5 = float(input("Enter grade for Module 5: "))
Module6 = float(input("Enter grade for Module 6: "))

#store grades in a list 
module_grades = [Module1, Module2, Module3, Module4, Module5, Module6]

#find lowest grade using min 
Lowest = min(module_grades)

#find highest grade using max 
Highest = max(module_grades)

#find the total using sum 
Total = sum(module_grades)

#caculate the average
Average = Total / len(module_grades)

#display the results

print("----------Results---------")
print(f"{"Lowest grade: ":<15}{Lowest}")
print(f"{"Highest grade: ":<15}{Highest}")
print(f"{"Sum of grades: ":<15}{Total}")
print(f"{"Average: ":<15}{Average:.2f}")
print("----------------------------")