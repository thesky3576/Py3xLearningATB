'''Write a program that calculates and displays the letter grade for a given numerical score (e.g., A, B, C, D, or F) based on the following grading scale:
input- score - 89
output- B
A: 90-100
B: 80-89
C: 70-79
D: 60-69
F: 0-59
'''
'''score = float(input("Enter the grade: "))
if score >= 90 and score <= 100:
    print("Your grade is : A")
elif score >= 80 and score <= 89:
    print("Your grade is : B")
elif score >= 70 and score <= 79:
    print("Your grade is : C")
elif score >= 60 and score <= 69:
    print("Your grade is : D")
elif score >= 0 and score <= 59:
    print("Your grade is : F")
else:
    print("invalid input")
    '''
def grade_calc(score):
    if score >= 90 and score <= 100:
        return "A"
    elif score >= 80 and score <= 89:
        return "B"
    elif score >= 70 and score <= 79:
        return "C"
    elif score >= 60 and score <= 69:
        return "D"
    elif score >= 0 and score <= 59:
        return "F"
    else:
        return "Invalid score"
    # Get the score from the user
score = float(input("Enter the grade: "))
# Call the grade_calc function and print the result
grade = grade_calc(score)
print("Your grade is:", grade)

