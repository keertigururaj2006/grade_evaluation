m1 = float(input("Enter subject 1 marks: "))
m2 = float(input("Enter subject 2 marks: "))
m3 = float(input("Enter subject 3 marks: "))
m4 = float(input("Enter subject 4 marks: "))
m5 = float(input("Enter subject 5 marks: "))

avg = (m1 + m2 + m3 + m4 + m5) / 5

print("Average =", avg)

if avg >= 90:
    print("Grade = A")
elif avg >= 75:
    print("Grade = B")
elif avg >= 60:
    print("Grade = C")
elif avg >= 45:
    print("Grade = D")
else:
    print("Grade = Fail")
