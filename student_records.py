import csv

def calculate_average_grade(filename):
    """Calculates the average grade of all students in the CSV file."""
    total_grades = 0
    num_students = 0

    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row
        for row in reader:
            name, age, grade = row
            total_grades += int(grade)
            num_students += 1

    return total_grades / num_students

def find_highest_grade_student(filename):
    """Finds the student with the highest grade in the CSV file."""
    highest_grade = 0
    highest_grade_student = None

    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row
        for row in reader:
            name, age, grade = row
            if int(grade) > highest_grade:
                highest_grade = int(grade)
                highest_grade_student = name

    return highest_grade_student

# Example usage
filename = 'student_records.csv'
average_grade = calculate_average_grade(filename)
highest_grade_student = find_highest_grade_student(filename)

print("Average Grade:", average_grade)
print("Student with Highest Grade:", highest_grade_student)