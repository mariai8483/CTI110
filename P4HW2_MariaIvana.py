#Ivana Maria
#4/6/2026
#P4HW2_MariaIvana
#salary calculator with loops 

# reguest employee info 
name = input("Enter employee's name or 'Done' to Terminate: ")

# create accumulator variables for overtime pay, regualr pay, gross pay and employee count 
overtimepay_total = 0
regularpay_total = 0 
grosspay_total = 0
employee_count = 0 

while name != "Done" :
     # add employee count plus one 
    employee_count += 1 
    # ask for employee info 
    hours = float(input("How many hours did " +name+ " work this week? "))
    rate = float(input("What is " +name+ "'s hourly pay rate? "))

    #cacluate pay 
    if hours > 40:
        overtime_hours = hours - 40 
        overtime_pay = overtime_hours * (rate * 1.5)
        regular_pay = 40 * rate 
        gross_pay = regular_pay + overtime_pay
    else:
        overtime_hours = 0
        overtime_pay = 0
        regular_pay = hours * rate 
        gross_pay = regular_pay
    # add to accumulator totals
    overtimepay_total += overtime_pay
    regularpay_total += regular_pay
    grosspay_total += gross_pay
    
#display results 
    print("----------------------------")
    print("Employee Name:", name)
    print(f'{"Hours Worked":<15}{"Pay Rate":<12}{"Overtime":<12}{"Overtime Pay":<15}{"Regular Pay":<15}{"Gross Pay":<12}')
    print("-----------------------------------------------------------------------------------------------")
    print(f'{hours:<15}{rate:<12}{overtime_hours:<12}{overtime_pay:<15}{regular_pay:<15}{gross_pay:<15}')
                                                                                               
    name = input("Enter employee's name or 'Done' to Terminate: ")

print("Total number of employees entered: ",employee_count)
print("Total amount paid for overtime: $", format(overtimepay_total, ',.2f'))
print("Total amount paid for regular time: $", format(regularpay_total, ',.2f'))
print("Total amount paid in gross: $", format(grosspay_total, ',.2f'))
