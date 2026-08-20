# ============================================================
# PYTHON FUNCTIONS
# Arguments + Variable Scope
# ============================================================


# ============================================================
# 1. BASIC FUNCTION
# ============================================================

def greet():
    print("Hello, Python!")


greet()


# Function with return value
def add(a, b):
    return a + b


result = add(10, 20)
print("Addition:", result)


# ============================================================
# 2. POSITIONAL ARGUMENT
# ============================================================

def student(name, age, course):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)


student("Aniket", 22, "Data Science")


# ============================================================
# 3. KEYWORD ARGUMENT
# ============================================================

def employee(name, salary, department):
    print("Name:", name)
    print("Salary:", salary)
    print("Department:", department)


employee(
    name="Aniket",
    salary=50000,
    department="Data Science"
)


# Keyword arguments can be passed in different order
employee(
    department="IT",
    name="Rahul",
    salary=60000
)


# ============================================================
# 4. DEFAULT ARGUMENT
# ============================================================

def greet_user(name="Guest"):
    print("Hello", name)


greet_user()
greet_user("Aniket")


def student_info(name, course="Python"):
    print("Name:", name)
    print("Course:", course)


student_info("Aniket")
student_info("Rahul", "Data Science")


# ============================================================
# 5. VARIABLE LENGTH ARGUMENT - *args
# ============================================================

def total(*args):
    print("Arguments:", args)
    print("Total:", sum(args))


total(10, 20)
total(10, 20, 30, 40, 50)


# *args with loop
def print_numbers(*args):
    for number in args:
        print(number)


print_numbers(10, 20, 30, 40)


# ============================================================
# 6. VARIABLE LENGTH KEYWORD ARGUMENT - **kwargs
# ============================================================

def student_details(**kwargs):

    for key, value in kwargs.items():
        print(key, ":", value)


student_details(
    name="Aniket",
    age=22,
    course="Data Science",
    city="Pune"
)


# ============================================================
# 7. *args + **kwargs TOGETHER
# ============================================================

def information(*args, **kwargs):

    print("Positional Arguments:", args)
    print("Keyword Arguments:", kwargs)


information(
    10,
    20,
    30,
    name="Aniket",
    course="Data Science"
)


# ============================================================
# 8. LOCAL SCOPE
# ============================================================

def local_example():

    message = "I am a local variable"

    print(message)


local_example()


# message cannot normally be accessed here
# print(message)


# ============================================================
# 9. ENCLOSING SCOPE
# ============================================================

def outer():

    message = "I am an enclosing variable"

    def inner():

        print(message)

    inner()


outer()


# ============================================================
# 10. NONLOCAL KEYWORD
# ============================================================

def counter():

    count = 0

    def increment():

        nonlocal count
        count += 1
        print("Count:", count)

    increment()
    increment()
    increment()


counter()


# ============================================================
# 11. GLOBAL SCOPE
# ============================================================

name = "Aniket"


def show_name():

    print("Global variable:", name)


show_name()


# Modifying global variable
count = 0


def increase_count():

    global count

    count += 1
    print("Count:", count)


increase_count()
increase_count()
increase_count()


# ============================================================
# 12. BUILT-IN SCOPE
# ============================================================

numbers = [10, 20, 30, 40, 50]


def built_in_example():

    print("Length:", len(numbers))
    print("Maximum:", max(numbers))
    print("Minimum:", min(numbers))
    print("Sum:", sum(numbers))


built_in_example()


# ============================================================
# 13. LEGB RULE
# ============================================================

x = "Global"


def outer_function():

    x = "Enclosing"

    def inner_function():

        x = "Local"

        print("Local:", x)

    inner_function()


outer_function()

print("Global:", x)


# ============================================================
# 14. FUNCTION WITH MULTIPLE ARGUMENT TYPES
# ============================================================

def profile(name, age=21, *skills, **details):

    print("\n--- Profile ---")
    print("Name:", name)
    print("Age:", age)
    print("Skills:", skills)
    print("Other Details:", details)


profile(
    "Aniket",
    22,
    "Python",
    "SQL",
    "Machine Learning",
    city="Pune",
    education="BSc"
)


# ============================================================
# 15. PRACTICAL EXAMPLE - STUDENT RESULT
# ============================================================

def calculate_total(*marks):

    return sum(marks)


def calculate_average(*marks):

    return sum(marks) / len(marks)


def student_result(name, *marks):

    total = calculate_total(*marks)
    average = calculate_average(*marks)

    print("\n--- Student Result ---")
    print("Name:", name)
    print("Marks:", marks)
    print("Total:", total)
    print("Average:", average)

    if average >= 75:
        print("Grade: A")
    elif average >= 60:
        print("Grade: B")
    elif average >= 40:
        print("Grade: C")
    else:
        print("Grade: F")


student_result(
    "Aniket",
    85,
    90,
    78,
    88,
    92
)


# ============================================================
# 16. FUNCTION RETURNING MULTIPLE VALUES
# ============================================================

def calculate(a, b):

    addition = a + b
    subtraction = a - b
    multiplication = a * b

    return addition, subtraction, multiplication


add_result, sub_result, mul_result = calculate(20, 10)

print("\n--- Calculations ---")
print("Addition:", add_result)
print("Subtraction:", sub_result)
print("Multiplication:", mul_result)

