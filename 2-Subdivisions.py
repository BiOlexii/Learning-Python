# ---------------------------------------------------------
# 1. ARITHMETIC OPERATORS
# ---------------------------------------------------------

# Regular Division (/) always returns a float (decimal)
print(3 / 2)   # Output: 1.5

# Floor Division (//) drops the decimal and returns an integer
print(3 // 2)  # Output: 1

# Exponent (**) is "to the power of"
print(3 ** 2)  # Output: 9 (3 squared)

# Modulus (%) returns only the REMAINDER
# Very useful for checking if a number is even (num % 2 == 0)
print(4 % 2)   # Output: 0 (4 is even)
print(5 % 2)   # Output: 1 (5 is odd)

# Order of Operations (BODMAS/PEMDAS)
# Multiplication/Division happen before Addition/Subtraction
print(1 + (3 * 2)) # Output: 7

# ---------------------------------------------------------
# 2. BUILT-IN NUMERIC FUNCTIONS
# ---------------------------------------------------------

# round(number, ndigits)
print(round(3.75))    # Output: 4 (rounds to nearest integer)
print(round(3.75, 1)) # Output: 3.8 (rounds to 1 decimal place)

# abs() returns the absolute value (removes the negative sign)
print(abs(-5))        # Output: 5

# ---------------------------------------------------------
# 3. COMPARISONS (Returns True or False)
# ---------------------------------------------------------

num_1 = 3
num_2 = 2

print(num_1 == num_2) # False (Are they equal?)
print(num_1 != num_2) # True  (Are they NOT equal?)
print(num_1 >= num_2) # True  (Greater than or equal to?)

# ---------------------------------------------------------
# 4. TYPE CASTING (Changing Strings to Numbers)
# ---------------------------------------------------------

num_a = '100'
num_b = '200'

# Without casting, Python treats these as text (Strings)
# '100' + '200' would result in '100200' (Concatenation)

num_a = int(num_a) # Converts string to Integer
num_b = int(num_b) 

print(num_a + num_b) # Output: 300
