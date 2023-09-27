grade = float(input("Enter your grade: "))
name = input("Enter your name: ")

highest_grade = grade
highest_grade_name = name

for i in range(9):

    name = input("Enter your name: ")
    grade = float(input("Enter your grade: "))

    while grade < 0 or grade > 100:
        print("Invalid grade")
        grade = float(input("Enter your a correct grade between 0 and 100: "))

    if grade > highest_grade:
        highest_grade = grade
        highest_grade_name = name


print(
    f"The highest grade is {highest_grade_name} with a grade of {highest_grade}")
