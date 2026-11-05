employees = [
    {"name": "Rahul", "department": "IT", "salary": 45000},
    {"name": "Priya", "department": "HR", "salary": 35000},
    {"name": "Aman", "department": "IT", "salary": 60000},
    {"name": "Sneha", "department": "Finance", "salary": 50000},
    {"name": "Karan", "department": "HR", "salary": 40000},
    {"name": "Neha", "department": "IT", "salary": 55000}
]
#Your tasks
#1. Find the employee with the highest salary.
#2. Calculate the average salary of all employees.
#3. Extract employees earning more than ₹45,000 using list comprehension.
#4. Group employees department-wise using a dictionary.
#5. Find the total salary expenditure of each department.
#6. Sort employees by salary in descending order using sorted() and lambda.

def highest_salary_employee(employees):
    return max(employees, key=lambda x: x['salary'])

def average_salary(employees):
    total_salary=sum(emp['salary'] for emp in employees)
    return total_salary/len(employees)

def earners(employees):
    return [emp['name'] for emp in employees if emp['salary'] > 45000]

def group_by_department(employees):
    department_dict={
        emp['department']: [emp for emp in employees if emp['department'] == emp['department']] for emp in employees
    }
    return department_dict

def total_salary_by_department(employees):
    department_salary={}
    for emp in employees:
        dept=emp['department']
        if dept in department_salary:
            department_salary[dept]+=emp['salary']
        else:
            department_salary[dept]=emp['salary']
    return department_salary

def sort_by_salary(employees):
    return sorted(employees, key=lambda x: x['salary'], reverse=True)



highest_salary_emp = highest_salary_employee(employees)
average_salary_value = average_salary(employees)
high_earners = earners(employees)
grouped_employees = group_by_department(employees)
total_salary_dept = total_salary_by_department(employees)
sorted_employees = sort_by_salary(employees)

employee_salary=dict(zip([emp['name'] for emp in employees], [emp['salary'] for emp in employees]))

print("Employee with the highest salary:\n", highest_salary_emp)
print("Average salary of all employees:\n", average_salary_value)
print("Employees earning more than ₹45,000:\n", high_earners)
print("Employees grouped by department:\n", grouped_employees)
print("Total salary expenditure by department:\n", total_salary_dept)
print("Employees sorted by salary in descending order:\n", sorted_employees)
print("Employee salaries:\n", employee_salary)