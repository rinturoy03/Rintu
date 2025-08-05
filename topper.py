students = {}
for i in range(5):
    name = input(f"Enter name of student {i+1}: ")
    marks = int(input(f"Enter marks of {name}: "))
    students[name] = marks
top_name = ""
top_marks = -1
for name in students:
    if students[name] > top_marks:
        top_name = name
        top_marks = students[name]
print(f"Topper is {top_name} with {top_marks} marks.")
