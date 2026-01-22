# ---------------------------------------------------------
# 1. THE BASIC IF STATEMENT
# ---------------------------------------------------------
# The code inside an 'if' block only runs if the condition is True.
if True:
   print('Conditional was True')

if False:
    print('Conditional was True') # This will never print.

# ---------------------------------------------------------
# 2. COMPARISON OPERATORS
# ---------------------------------------------------------
# Comparisons:
# Equal:              ==
# Not Equal:          !=
# Greater Than:       >
# Less Than:          <
# Greater or Equal:   >=
# Less or Equal:      <=
# Object Identity:    is

language = 'Python'

if language == 'Python':
  print('Conditional was True')

# ---------------------------------------------------------
# 3. ELIF AND ELSE (The Decision Tree)
# ---------------------------------------------------------
# Use 'elif' (else if) to check multiple conditions in order.
# Use 'else' as a "catch-all" if none of the above are True.



# Ex.1
if language == 'Python':
  print('Language is Python')
else:
  print('No match')

# Ex.2 Since first statement is correct else is not printed, but if it was false
if language == 'Java':
  print('Language is Python')
else:
  print('No match')

# What if we need check for different languages at the same time?
if language == 'Python':
  print('Language is Python')
elif language == 'Java':
  print('Language is Java')
elif language == 'JavaScript':
  print('Language is JavaScript')
else:
  print('No match')

# ---------------------------------------------------------
# 4. BOOLEAN OPERATORS (Logical Gates)
# ---------------------------------------------------------
# AND: Both must be True
# OR:  At least one must be True
# NOT: Flips the result (True becomes False)

# --- and command ---
user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
   print('Admin Page') # Both are True, so this prints.
else:
  print('Bad Creds')

# Ex.2 one of them if false
logged_in = False
if user == 'Admin' and logged_in:
   print('Admin Page')
else:
  print('Bad Creds') # logged_in is False, so the whole 'and' is False.

# --- or command ---
user = 'Admin'
logged_in = False

if user == 'Admin' or logged_in:
   print('Admin Page') # This prints because at least one (user) is True.
else:
  print('Bad Creds')

# --- not command ---
# Ex.1 if not false where outcome is True
user = 'Admin'
logged_in = True

if not logged_in:
   print('Please Log In')
else:
  print('Welcome!')

# Ex.2 if not false where outcome is False
user = 'Admin'
logged_in = False

if not logged_in:
   print('Please Log In')
else:
  print('Welcome!')

# ---------------------------------------------------------
# 5. EQUALITY (==) VS IDENTITY (is)
# ---------------------------------------------------------
# '==' checks if the VALUES are the same.
# 'is' checks if they are the EXACT SAME OBJECT in memory (memory address).

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)    # True: The lists look the same.
print(a is b)    # False: They are two different lists stored in different spots.

print(id(a))     # Unique memory address for a
print(id(b))     # Unique memory address for b (different from a)

print(a is not b) # True

# If we point 'b' to the same object as 'a':
b = a
print(id(a))
print(id(b))     # Now these IDs match exactly.
print(id(a) == id(b))
print(a is b)    # True
print(a == b)    # True

# ---------------------------------------------------------
# 6. FALSY VALUES (What Python considers "False")
# ---------------------------------------------------------
# In Python, you don't always have to compare to True or False. 
# Empty objects and zeros are automatically "False".

# Ex.1 False
condition = False
if condition:
  print('Evaluated to True')
else:
  print('Evaluated to False')

# Ex.2 None (Used to represent the absence of a value)
condition = None
if condition:
  print('Evaluated to True')
else:
  print('Evaluated to False')

# Ex.3 Zero of any numeric type
condition = 0 
if condition:
  print('Evaluated to True')
else:
  print('Evaluated to False')

# Ex.4 Any empty sequence. For example, '', (), [].
condition = '' 
if condition:
  print('Evaluated to True')
else:
  print('Evaluated to False')

# Ex.5 Any empty mapping. For example, {}.
condition = {}
if condition:
  print('Evaluated to True')
else:
  print('Evaluated to False')

# ---------------------------------------------------------
# 7. TRUTHY VALUES
# ---------------------------------------------------------
# Anything not in the "False" list above is True.
condition = 'Test' # A non-empty string is True
if condition:
  print('Evaluated to True')
else:
  print('Evaluated to False')
