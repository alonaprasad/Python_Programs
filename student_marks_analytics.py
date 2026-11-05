# Student Marks Analytics
# A beginner-friendly Python project using lists, tuples, sets and dictionaries.

# A tuple stores fixed subject names.
subjects = ("Python", "Mathematics", "Computer Science")

# A list stores the students' records.
students = [
    {"name": "Asha", "marks": [85, 90, 88]},
    {"name": "Ravi", "marks": [72, 80, 75]},
    {"name": "Neha", "marks": [95, 92, 96]}
]

# A set stores unique subject names.
unique_subjects = set(subjects)


# This function calculates the average marks.
def calculate_average(marks):
    total = sum(marks)
    average = total / len(marks)
    return average


# This function assigns a grade using if-elif-else.
def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    else:
        return "Needs improvement"


# A dictionary will store each student's average.
student_averages = {}

print("===== STUDENT MARKS ANALYTICS =====")
print("Subjects:", subjects)
print("Unique subjects:", unique_subjects)
print()

# A for loop processes each student's dictionary.
for student in students:
    name = student["name"]
    marks = student["marks"]

    average = calculate_average(marks)
    grade = calculate_grade(average)

    # Add the student's average to a dictionary.
    student_averages[name] = average

    print("Student:", name)
    print("Marks:", marks)

    # Display each subject and its corresponding mark.
    for index in range(len(subjects)):
        print(subjects[index], ":", marks[index])

    print("Total:", sum(marks))
    print("Average:", round(average, 2))
    print("Grade:", grade)
    print("------------------------------")


# Find the student with the highest average.
top_student = max(student_averages, key=student_averages.get)

print("===== CLASS SUMMARY =====")
print("Student averages:", student_averages)
print("Top-performing student:", top_student)
print("Highest average:", round(student_averages[top_student], 2))
