students = {}

# input data for 5 students
for i in range(5):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks

# find class average
total = sum(students.values())
average = total / len(students)

# find topper
topper = max(students, key=students.get)

# assign grades
print("\nStudent Grades:")
for name, marks in students.items():
    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    else:
        grade = "D"
    
    print(name, "-", marks, "-", grade)

print("\nClass Average:", average)
print("Topper:", topper, "with", students[topper], "marks")