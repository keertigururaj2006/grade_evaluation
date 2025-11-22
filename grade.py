import sys

# Expecting 5 marks as command-line arguments
if len(sys.argv) != 6:
    print("Usage: python marks.py <m1> <m2> <m3> <m4> <m5>")
    sys.exit(1)

# Read marks from arguments
m1 = float(sys.argv[1])
m2 = float(sys.argv[2])
m3 = float(sys.argv[3])
m4 = float(sys.argv[4])
m5 = float(sys.argv[5])

avg = (m1 + m2 + m3 + m4 + m5) / 5
print("Average Marks:", avg)

# Grade logic
if avg >= 90:
    grade = "A"
elif avg >= 75:
    grade = "B"
elif avg >= 60:
    grade = "C"
elif avg >= 45:
    grade = "D"
else:
    grade = "Fail"

print("Grade:", grade)
