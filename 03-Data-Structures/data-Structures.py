# ==========================================
# Python Data Structures - 
# ==========================================


# =========================
# 1. LIST
# =========================

numbers = [10, 20, 30, 20, 40]

print("\n--- LIST ---")
print("Original:", numbers)

numbers.append(50)
print("append:", numbers)

numbers.insert(1, 15)
print("insert:", numbers)

numbers.remove(20)
print("remove:", numbers)

numbers.pop()
print("pop:", numbers)

print("count:", numbers.count(20))
print("index:", numbers.index(30))

numbers.sort()
print("sort:", numbers)

numbers.reverse()
print("reverse:", numbers)

print("length:", len(numbers))


# =========================
# 2. TUPLE
# =========================

data = (10, 20, 30, 20, 40)

print("\n--- TUPLE ---")
print("Tuple:", data)

print("count:", data.count(20))
print("index:", data.index(30))
print("length:", len(data))


# =========================
# 3. SET
# =========================

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("\n--- SET ---")

a.add(5)
print("add:", a)

a.remove(2)
print("remove:", a)

print("union:", a.union(b))
print("intersection:", a.intersection(b))
print("difference:", a.difference(b))

print("subset:", {3, 4}.issubset(a))
print("superset:", a.issuperset({3, 4}))


# =========================
# 4. DICTIONARY
# =========================

student = {
    "name": "Aniket",
    "age": 21,
    "course": "Data Science"
}

print("\n--- DICTIONARY ---")
print("Dictionary:", student)

print("keys:", student.keys())
print("values:", student.values())
print("items:", student.items())

print("get name:", student.get("name"))

student.update({"city": "Pune"})
print("update:", student)

student.pop("age")
print("pop:", student)

print("length:", len(student))