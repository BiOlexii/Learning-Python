# ---------------------------------------------------------
# 1. STRING BASICS & ESCAPING
# ---------------------------------------------------------

# Use double quotes if your string contains a single quote
message = "Bobby's World" 

# OR use a backslash (\) to 'escape' the character so Python doesn't get confused
message = 'Bobby\'s World' 

message = 'Hello World'

# ---------------------------------------------------------
# 2. SLICING AND INDEXING
# ---------------------------------------------------------
# Python is "0-indexed," meaning the first character is at position 0.


print(f"Original: {message}")
print(message[0])      # Output: H (First character)
print(message[0:5])    # Output: Hello (Starts at 0, stops BEFORE index 5)
print(message[6:])     # Output: World (Starts at 6 and goes to the end)

# ---------------------------------------------------------
# 3. USEFUL STRING METHODS
# ---------------------------------------------------------

print(len(message))       # Returns the total length (11)
print(message.lower())    # All lowercase
print(message.upper())    # All uppercase
print(message.count('l')) # Returns 3 (counts how many 'l's exist)
print(message.find('orl'))# Returns 7 (the index where that pattern starts)

# Replace 'World' with 'Universe'
# Note: Strings are immutable, so you must assign the result to a new variable
new_message = message.replace('World', 'Universe')
print(new_message)

# ---------------------------------------------------------
# 4. STRING CONCATENATION & FORMATTING
# ---------------------------------------------------------

greeting = 'Hello'
name = 'Michael'

# The modern, preferred way: F-Strings (Formatted Strings)
# You can put variables or even functions directly inside the curly braces
other_message = f'{greeting}, {name.upper()}. Welcome!'
print(other_message)

# ---------------------------------------------------------
# 5. DISCOVERY TOOLS (The "How do I do X?" tools)
# ---------------------------------------------------------

# dir() shows you ALL the methods available for a specific object/variable
# print(dir(name)) 

# help() gives you the actual documentation for a specific method
# print(help(str.lower))
