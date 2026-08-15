# ==========================================
# Python Strings
# Indexing, Slicing & String Methods
# ==========================================


# -------------------------------
# 1. Indexing
# -------------------------------

text = "Python Programming"

print("First character:", text[0])
print("Last character:", text[-1])
print("Third character:", text[2])
print("Fifth character:", text[4])
print("Second-last character:", text[-2])


# -------------------------------
# 2. Slicing
# -------------------------------

text = "Python Programming"

print("First 6 characters:", text[:6])
print("Last 11 characters:", text[7:])
print("Characters 2 to 8:", text[2:9])
print("Every 2nd character:", text[::2])
print("Reverse:", text[::-1])


# -------------------------------
# 3. Upper / Lower / Title
# -------------------------------

text = "python programming"

print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Title Case:", text.title())
print("Capitalized:", text.capitalize())


# -------------------------------
# 4. Strip
# -------------------------------

text = "   Python Programming   "

print("Original:", text)
print("Strip:", text.strip())
print("Left Strip:", text.lstrip())
print("Right Strip:", text.rstrip())


# -------------------------------
# 5. Count
# -------------------------------

text = "Python Programming"

print("Count of 'o':", text.count("o"))
print("Count of 'm':", text.count("m"))


# -------------------------------
# 6. Find
# -------------------------------

text = "I love Python Programming"

print("Position of Python:", text.find("Python"))
print("Position of Programming:", text.find("Programming"))


# -------------------------------
# 7. Replace
# -------------------------------

text = "Python is easy"

print(text.replace("easy", "powerful"))
print(text.replace("Python", "Data Science"))


# -------------------------------
# 8. Startswith / Endswith
# -------------------------------

text = "Python Programming"

print("Starts with Python:", text.startswith("Python"))
print("Ends with Programming:", text.endswith("Programming"))


# -------------------------------
# 9. String Checking Methods
# -------------------------------

text1 = "Python"

print("isalpha:", text1.isalpha())

text2 = "Python123"

print("isalnum:", text2.isalnum())

text3 = "12345"

print("isdigit:", text3.isdigit())

text4 = "python"

print("islower:", text4.islower())

text5 = "PYTHON"

print("isupper:", text5.isupper())


# -------------------------------
# 10. Split
# -------------------------------

text = "Python is easy to learn"

words = text.split()

print("Split:", words)


# -------------------------------
# 11. Join
# -------------------------------

words = ["Python", "is", "powerful"]

result = " ".join(words)

print("Joined:", result)


# -------------------------------
# 12. Mixed Practice
# -------------------------------

text = "  Python is Powerful and Easy to Learn  "

print("\n--- String Analyzer ---")

print("Original:", text)
print("Strip:", text.strip())
print("Upper:", text.upper())
print("Lower:", text.lower())
print("Title:", text.title())
print("First character:", text.strip()[0])
print("Last character:", text.strip()[-1])
print("First 6 characters:", text.strip()[:6])
print("Last 5 characters:", text.strip()[-5:])
print("Reverse:", text.strip()[::-1])
print("Count of 'o':", text.count("o"))
print("Position of Powerful:", text.find("Powerful"))
print("Replace Python:", text.replace("Python", "Data Science"))
print("Words:", text.split())