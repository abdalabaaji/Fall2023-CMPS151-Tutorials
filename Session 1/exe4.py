
total_salary_dept_1 = 0
total_salary_dept_2 = 0

total_emp_dep_1 = 0
total_emp_dep_2 = 0

for i in range(10):
    dept_no = int(input("Enter department number [1 or 2]: "))
    salary = int(input("Enter salary : "))

    # validation
    while dept_no != 1 and dept_no != 2:
        print("Invalid department number")
        dept_no = int(input("Enter again department number : "))

    if dept_no == 1:
        total_salary_dept_1 += salary
        total_emp_dep_1 += 1
    else:
        total_salary_dept_2 += salary
        total_emp_dep_2 += 1

avg_dep_1 = total_salary_dept_1 / total_emp_dep_1
avg_dep_2 = total_salary_dept_2 / total_emp_dep_2

print("Average salary of department 1 : ", avg_dep_1)
print("Average salary of department 2 : ", avg_dep_2)
