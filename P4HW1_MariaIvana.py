#Ivana Maria
#4/12/26
#P4HW1
#ability to edit and enchance existing program

#ask how many scores
num_scores = int(input("How many scores do you want to enter? "))

#create an empty list to store valid scores 
score_list = []

#use a loop to collect each score 
for i in range (1, num_scores + 1):
    #ask the user to enter a score 
    score = float(input(f"Enter score #{i}: "))
    
    #ask until the score is between 0 and 100
    while score < 0 or score > 100:
        print("INVALID Score entered!!!!")
        print("Score should be between 0 and 100")

        #if not valid ask for the same score again 
        score = float(input(f"Enter score #{i} again: "))
    #add the valid score 
    score_list.append(score)

#find the lowest score 
lowest_score = min(score_list)

#remove the lowest score from the list 
score_list.remove(lowest_score)

#caculate the average 
average = sum(score_list) / len(score_list)

#determine the letter grade
if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

#display result 
print("------------Results------------------------")
print(f"{"Lowest score ":<15}: {lowest_score}")
print(f"{"Modified List " :<15}: {score_list}")
print(f"{"Scores Average ":<15}: {average:.2f}")
print(f"{"Grade ":<15}: {grade}")
print("---------------------------------------------")