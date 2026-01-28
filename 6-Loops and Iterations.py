# ---------------------------------------------------------
# 1. FOR LOOPS (Iterating through Sequences)
# ---------------------------------------------------------
nums = [1, 2, 3, 4, 5]

# A basic loop: 'num' is a temporary variable that holds the current item
for num in nums:
    print(num)

# --- The Break Statement ---
# Use 'break' to exit the loop entirely when a condition is met.
for num in nums:
    if num == 3:
        print('Found!')
        break  # This stops the loop; 4 and 5 will never be printed.
    print(num)

# --- The Continue Keyword ---
# Use 'continue' to skip the current iteration and move to the next item.
for num in nums:
    if num == 3:
        print('Found!')
        continue  # This skips printing '3', but continues with 4 and 5.
    print(num)



# ---------------------------------------------------------
# 2. NESTED LOOPS (Loops inside Loops)
# ---------------------------------------------------------
# This is useful for combinations (like coordinates or grid systems).
for num in nums:
    for letter in 'abc':
        print(num, letter) # Runs 15 times (5 numbers * 3 letters)

# ---------------------------------------------------------
# 3. THE RANGE() FUNCTION
# ---------------------------------------------------------
# range(start, stop, step)
# Note: The 'stop' value is NOT included.

for i in range(10):      # Starts at 0, ends at 9
    print(i)

for i in range(1, 11):   # Starts at 1, ends at 10
    print(i)

# ---------------------------------------------------------
# 4. WHILE LOOPS (Running until a Condition is False)
# ---------------------------------------------------------
x = 0

# Be careful: If the condition never becomes False, you get an "Infinite Loop"!
while x < 10:
    print(x)
    x += 1  # Standard increment. Without this, x stays 0 and the loop never ends.

# --- While loop with Break ---
x = 0
while x < 10:
    if x == 5:
        break # Stops when x hits 5
    print(x)
    x += 1

# --- The "Infinite" Loop Pattern ---
# Common in programs that wait for user input (like a game loop).
x = 0
while True: # This loop runs forever...
    if x == 5:
        break # ...until this break is triggered.
    print(x)
    x += 1
