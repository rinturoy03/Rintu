marks = []
for i in range(5):
    m = int(input(f"Enter marks of student {i+1}: "))
    marks.append(m)
print("\nMarks of 5 students:")
for i in range(5):
    print(f"Student {i+1}: {marks[i]}")
