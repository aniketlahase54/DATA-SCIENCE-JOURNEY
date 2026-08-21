

# ============================================================
# 1. BASIC LAMBDA FUNCTION
# ============================================================

square = lambda x: x ** 2

print("Square:", square(5))


# ============================================================
# 2. LAMBDA WITH ONE ARGUMENT
# ============================================================

double = lambda x: x * 2

print("Double:", double(10))


# ============================================================
# 3. LAMBDA WITH MULTIPLE ARGUMENTS
# ============================================================

add = lambda a, b: a + b

print("Addition:", add(10, 20))


subtract = lambda a, b: a - b

print("Subtraction:", subtract(20, 10))


multiply = lambda a, b: a * b

print("Multiplication:", multiply(10, 5))


divide = lambda a, b: a / b

print("Division:", divide(20, 5))


# ============================================================
# 4. LAMBDA WITH CONDITIONAL EXPRESSION
# ============================================================

even_odd = lambda x: "Even" if x % 2 == 0 else "Odd"

print("Number:", even_odd(10))
print("Number:", even_odd(7))


# ============================================================
# 5. LAMBDA WITH STRINGS
# ============================================================

uppercase = lambda text: text.upper()

print("Uppercase:", uppercase("python"))


lowercase = lambda text: text.lower()

print("Lowercase:", lowercase("PYTHON"))


string_length = lambda text: len(text)

print("Length:", string_length("Data Science"))


# ============================================================
# 6. LAMBDA WITH LIST
# ============================================================

numbers = [1, 2, 3, 4, 5]

square_numbers = list(map(lambda x: x ** 2, numbers))

print("Squares:", square_numbers)


# ============================================================
# 7. MAP() WITH LAMBDA
# ============================================================

numbers = [10, 20, 30, 40, 50]

double_numbers = list(map(lambda x: x * 2, numbers))

print("Doubled:", double_numbers)


# Convert Celsius to Fahrenheit

celsius = [0, 10, 20, 30, 40]

fahrenheit = list(
    map(lambda c: (c * 9 / 5) + 32, celsius)
)

print("Fahrenheit:", fahrenheit)


# ============================================================
# 8. FILTER() WITH LAMBDA
# ============================================================

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = list(
    filter(lambda x: x % 2 == 0, numbers)
)

print("Even Numbers:", even_numbers)


odd_numbers = list(
    filter(lambda x: x % 2 != 0, numbers)
)

print("Odd Numbers:", odd_numbers)


# Numbers greater than 5

greater_than_five = list(
    filter(lambda x: x > 5, numbers)
)

print("Greater than 5:", greater_than_five)


# ============================================================
# 9. REDUCE() WITH LAMBDA
# ============================================================

from functools import reduce

numbers = [1, 2, 3, 4, 5]

total = reduce(
    lambda a, b: a + b,
    numbers
)

print("Total:", total)


product = reduce(
    lambda a, b: a * b,
    numbers
)

print("Product:", product)


# ============================================================
# 10. SORTED() WITH LAMBDA
# ============================================================

numbers = [50, 10, 40, 20, 30]

ascending = sorted(
    numbers,
    key=lambda x: x
)

print("Ascending:", ascending)


descending = sorted(
    numbers,
    key=lambda x: x,
    reverse=True
)

print("Descending:", descending)


# ============================================================
# 11. SORT STRINGS BY LENGTH
# ============================================================

names = ["Aniket", "Raj", "Amit", "Christopher"]

sorted_names = sorted(
    names,
    key=lambda name: len(name)
)

print("Sorted by length:", sorted_names)


# ============================================================
# 12. SORT TUPLES
# ============================================================

students = [
    ("Aniket", 85),
    ("Rahul", 92),
    ("Amit", 75),
    ("Sneha", 88)
]

students_by_marks = sorted(
    students,
    key=lambda student: student[1]
)

print("Students by marks:", students_by_marks)


# ============================================================
# 13. SORT DICTIONARY DATA
# ============================================================

employees = [
    {"name": "Aniket", "salary": 50000},
    {"name": "Rahul", "salary": 70000},
    {"name": "Amit", "salary": 45000}
]

employees_by_salary = sorted(
    employees,
    key=lambda employee: employee["salary"]
)

print("Employees by salary:")

for employee in employees_by_salary:
    print(employee)


# ============================================================
# 14. LAMBDA WITH MULTIPLE CONDITIONS
# ============================================================

check_number = lambda x: (
    "Positive" if x > 0
    else "Negative" if x < 0
    else "Zero"
)

print(check_number(10))
print(check_number(-5))
print(check_number(0))


# ============================================================
# 15. PRACTICAL EXAMPLE - STUDENT RESULT
# ============================================================

marks = [85, 72, 91, 65, 38, 95]

passed_students = list(
    filter(lambda mark: mark >= 40, marks)
)

print("Passed Marks:", passed_students)


grades = list(
    map(
        lambda mark:
        "A" if mark >= 80
        else "B" if mark >= 60
        else "C" if mark >= 40
        else "F",
        marks
    )
)

print("Grades:", grades)


# ============================================================
# 16. PRACTICAL DATA SCIENCE EXAMPLE
# ============================================================

data = [10, 20, 30, 40, 50]

# Add 10% to every value
updated_data = list(
    map(lambda x: x * 1.10, data)
)

print("Updated Data:", updated_data)


# Filter values greater than average
average = sum(data) / len(data)

above_average = list(
    filter(lambda x: x > average, data)
)

print("Average:", average)
print("Above Average:", above_average)

