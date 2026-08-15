# exp 1
# def sq(x):
#     return x * x

# square=sq(5)
# print("Square of 5 is:",square)


# exp 2
# def even_odd(x):
#     if x%2==0:
#         return True
#     else:
#         return False

# ans=even_odd(8)
# print("The number is:",ans)



# exp 3
# def find(numbers):
#     greater=numbers[0]
#     for num in numbers:
#         if num>greater:
#             greater=num
#     return greater

# result=find([10, 50, 20, 80, 30])
# print("The greatest number is:", result)



# exp 4
# def get_dep(employees):
#     for emp in employees:
#         if emp["department"]=="Data":
#             print(emp)


# employees = [
#     {"name": "Ali", "salary": 70000, "department": "IT"},
#     {"name": "Ahmed", "salary": 85000, "department": "Data"},
#     {"name": "Sara", "salary": 90000, "department": "Data"},
#     {"name": "Usman", "salary": 60000, "department": "HR"}
# ]

# get_dep(employees)


# exp 5

# def avg(numbers):
#     total=0
#     for num in numbers:
#         total+=num
#     return total/len(numbers)

# result=avg([10, 20, 30, 40, 50])
# print("The average is:", result)



transactions = [
    {"user": "Ali", "amount": 500},
    {"user": "Ahmed", "amount": 1000},
    {"user": "Ali", "amount": 700},
    {"user": "Sara", "amount": 300},
    {"user": "Ahmed", "amount": 500},
    {"user": "Ali", "amount": 800}
]

def analyze_transactions(transactions):
    total={}
    for transaction in transactions:
        user=transaction["user"]
        amount=transaction["amount"]
        if user in total:
            total[user]+=amount
        else:
            total[user]=amount

    return total

analysis=analyze_transactions(transactions)
print(analysis)