# 1. Basic List Comprehension
numbers = [1, 2, 3, 4, 5]

squares = [x ** 2 for x in numbers]

print(squares)
# [1, 4, 9, 16, 25]


# 2. Using range()
numbers = [x for x in range(1, 11)]

print(numbers)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# 3. List Comprehension with if
numbers = range(1, 21)

even = [x for x in numbers if x % 2 == 0]

print(even)
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


# 4. if-else Condition
numbers = [1, 2, 3, 4, 5, 6]

result = ["Even" if x % 2 == 0 else "Odd" for x in numbers]

print(result)
# ['Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even']


# 5. String List Comprehension
names = ["aniket", "rahul", "amit", "sneha"]

upper_names = [name.upper() for name in names]

print(upper_names)
# ['ANIKET', 'RAHUL', 'AMIT', 'SNEHA']


# 6. String with Condition
names = ["aniket", "rahul", "amit", "sneha"]

upper_names = [name.upper() for name in names]

print(upper_names)
# ['ANIKET', 'RAHUL', 'AMIT', 'SNEHA']


# 7. Extract Vowels from String
text = "Python Programming"

vowels = [ch for ch in text if ch.lower() in "aeiou"]

print(vowels)
# ['o', 'o', 'a', 'i']


# 8. Nested List Comprehension
matrix = [[1, 2], [3, 4], [5, 6]]

result = [num for row in matrix for num in row]

print(result)
# [1, 2, 3, 4, 5, 6]


# 9. Nested Loop + Condition
numbers = [1, 2, 3, 4]
letters = ["A", "B"]

result = [(num, letter) 
          for num in numbers 
          for letter in letters 
          if num % 2 == 0]

print(result)
# [(2, 'A'), (2, 'B'), (4, 'A'), (4, 'B')]


# 10. List Comprehension with Function
def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]

result = [square(x) for x in numbers]

print(result)
# [1, 4, 9, 16, 25]
