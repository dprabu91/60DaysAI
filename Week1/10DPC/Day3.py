# Condtional Statements Example
'''
score = int(input("Enter your score: "))

if score >= 90 and score <= 100:
    grade = 'A'
elif score >= 80 and score < 90:
    grade = 'B' 
elif score >= 70 and score < 80:
    grade = 'C'
elif score >= 60 and score < 70:
    grade = 'D'
else:
    grade = 'F'

print(f"Your grade is: {grade}")

'''

age = int(input("Enter your age: "))

Pro = input ("Are you a professional? (yes/no): ")

if age >= 18:
    if Pro.lower() == 'yes':
        print("You are eligible for the professional membership.")
    else:
        print("You are eligible for the regular membership.")
else:
    print("You are not eligible for membership.")   

status = "Member" if age >= 18 else "Non-Member"
print(f"Your status is: {status}")