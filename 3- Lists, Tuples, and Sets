# ---------------------------------------------------------
# 1. LISTS (Ordered, Mutable, Allows Duplicates)
# ---------------------------------------------------------
courses = ['History', 'Math', 'Physics', 'CompSci']
extra_courses = ['Art', 'Education']

# Adding Items
courses.append('Design')      # Adds to the very end
courses.insert(0, 'Biology')  # Adds to a specific index (0 = start)
courses.extend(extra_courses) # Merges the two lists into one

# Removing Items
courses.remove('Math')        # Removes specific value
popped = courses.pop()        # Removes AND returns the last item (useful for stacks)

# Slicing (Same as strings)
# [start:stop:step]
print(courses[0:2])           # First two items
print(courses[-1])            # The last item

# Sorting
nums = [1, 5, 3, 4, 2]
nums.sort()                   # Sorts the original list "in-place"
sorted_list = sorted(nums)    # Returns a NEW sorted list (original stays same)

# ---------------------------------------------------------
# 2. LOOPS & STRING CONVERSION
# ---------------------------------------------------------

# enumerate gives you both the index and the value
for index, course in enumerate(courses, start=1):
    print(f"Course {index}: {course}")

# Turning a list into a string
course_str = ', '.join(courses) 

# Turning a string back into a list
new_list = course_str.split(', ')

# ---------------------------------------------------------
# 3. TUPLES (Ordered, IMMUTABLE, Allows Duplicates)
# ---------------------------------------------------------
# Use Tuples when you have data that should NOT change (e.g., coordinates)

tuple_1 = ('History', 'Math', 'Physics')
# tuple_1[0] = 'Art'  # This would trigger a TypeError!

# ---------------------------------------------------------
# 4. SETS (Unordered, Unique, No Duplicates)
# ---------------------------------------------------------
# Sets are optimized for "Membership Tests" (checking if something is inside)
# and finding similarities/differences between groups.

cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}



[Image of Venn diagram showing set intersection, union, and difference]


print(cs_courses.intersection(art_courses)) # Shared items: {'Math', 'History'}
print(cs_courses.difference(art_courses))   # In CS but not Art: {'Physics', 'CompSci'}
print(cs_courses.union(art_courses))        # All unique items from both

# ---------------------------------------------------------
# 5. INITIALIZING EMPTY OBJECTS
# ---------------------------------------------------------

empty_list = []
empty_tuple = ()
empty_set = set() # Note: {} creates an empty Dictionary, not a Set!
