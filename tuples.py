# exercise 1

# student=("Huzaifa",21,"Bahria university","BSE")

# name,age,university,degree=student

# print(name)
# print(age)
# print(university)
# print(degree)


# exercise 2
# numbers = [1, 2, 2, 3, 4, 4, 5, 5, 5, 6]
# num=set(numbers)
# print(num)
# count=0
# for i in num:
#     count+=1
# print("The number of unique elements in the list is:",count)

# exercise 3
# python = {"Ali", "Ahmed", "Huzaifa", "Usman"}
# sql = {"Huzaifa", "Usman", "Hamza"}

# print("Students who know both Python and SQL:", python.intersection(sql))
# print("Students who know only Python:", python - sql)
# print("Unique students who know either Python or SQL:", python.union(sql))


# exercise 4
# student={
#     "name": "Huzaifa",
#     "age": 21,
#     "semester": 5,
#     "cgpa": 3.5,
#     "university": "Bahria University"
# }

# print("Student Name:",student["name"])
# student["cgpa"]=3.8
# remove_key="age"
# del student[remove_key]

# if "email" in student:
#     print("FOUND")
# else:
#     print("NOT FOUND")


# exercise 5
employees = [
    {"name": "Ali", "salary": 70000, "department": "IT"},
    {"name": "Ahmed", "salary": 85000, "department": "Data"},
    {"name": "Sara", "salary": 90000, "department": "Data"},
    {"name": "Usman", "salary": 60000, "department": "HR"}
]


for employee in employees:
    print("Name:",employee["name"])

for employee in employees:
    if employee["department"]=="Data":
        print(employee["name"])

total_salary=0

for employee in employees:
    total_salary+=employee["salary"]

print("Total Salary of all employees:",total_salary)



highest=employees[0]

for employee in employees:
    if employee["salary"]>highest["salary"]:
        highest=employee

print("Employee with the highest salary:",employee["name"])
