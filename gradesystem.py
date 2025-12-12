marks = [78, 88, 90, 900]
avg = sum(marks) / len(marks)

if avg >= 90:
    grade = "A"
elif avg >= 75:
    grade = "B"
else:
    grade = "C"

print("Average:", avg, "Grade:", grade)
