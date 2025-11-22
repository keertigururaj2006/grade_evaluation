# Accept marks of 5 subjects and calculate average + grade

marks = []
for i in range(1, 6):
    m = float(input(f"Enter marks of subject {i}: "))
    marks.append(m)

average = sum(marks) / 5
print("Average Marks =", average)

# Decide grade
if average >= 90:
    grade = 'A'
elif average >= 75:
    grade = 'B'
elif average >= 60:
    grade = 'C'
elif average >= 45:
    grade = 'D'
else:
    grade = 'Fail'

print("Grade =", grade)
