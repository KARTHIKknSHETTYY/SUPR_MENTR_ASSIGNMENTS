import matplotlib.pyplot as plt

# example dataset (marks of students)
marks = [65, 70, 75, 80, 85, 90, 60, 72, 88, 95]

# Bar Chart
students = ["S1","S2","S3","S4","S5","S6","S7","S8","S9","S10"]
plt.bar(students, marks)
plt.title("Student Marks - Bar Chart")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# Pie Chart
labels = ["Below 70", "70-85", "Above 85"]
sizes = [2, 5, 3]
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Marks Distribution - Pie Chart")
plt.show()

# Histogram
plt.hist(marks, bins=5)
plt.title("Marks Distribution - Histogram")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()