# ---------------------------------------------------------
# 1. DICTIONARY BASICS
# ---------------------------------------------------------
# Keys must be unique and immutable (usually strings or integers)
student = {
    'name': 'John', 
    'age': 25, 
    'courses': ['Math', 'CompSci']
}

# Accessing values
print(student['name'])  # Output: John

# ---------------------------------------------------------
# 2. SAFE ACCESS WITH .GET()
# ---------------------------------------------------------
# Using student['phone'] would cause a KeyError if the key doesn't exist.
# .get() is safer because it returns 'None' instead of crashing.

print(student.get('phone'))           # Output: None
print(student.get('phone', 'N/A'))    # Output: N/A (Custom default value)

# ---------------------------------------------------------
# 3. ADDING AND UPDATING
# ---------------------------------------------------------

# Adding/Updating a single value
student['phone'] = '555-5555'
student['name'] = 'Jane'

# Updating multiple values at once using .update()
# This is efficient for merging data into your dictionary.
student.update({
    'name': 'Jane Doe', 
    'age': 26, 
    'email': 'jane@example.com'
})

print(student)

# ---------------------------------------------------------
# 4. REMOVING DATA
# ---------------------------------------------------------

# Option 1: del keyword (removes permanently)
# del student['age']

# Option 2: .pop() (removes and saves the value to a variable)
age = student.pop('age') 
print(f"Removed age: {age}")

# ---------------------------------------------------------
# 5. KEYS, VALUES, AND ITEMS
# ---------------------------------------------------------

print(len(student))      # Number of keys in the dictionary
print(student.keys())    # List of all keys
print(student.values())  # List of all values
print(student.items())   # List of (key, value) pairs as tuples

# ---------------------------------------------------------
# 6. LOOPING THROUGH DICTIONARIES
# ---------------------------------------------------------

# Looping through keys only
for key in student:
    print(f"Key: {key}")

# Looping through both Keys and Values (Most common)
# We use "unpacking" to assign the key and value to variables simultaneously.
for key, value in student.items():
    print(f"{key}: {value}")
