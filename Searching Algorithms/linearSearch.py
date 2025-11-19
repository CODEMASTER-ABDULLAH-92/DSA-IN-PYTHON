# =====================================================
# LINEAR SEARCH IN PYTHON
# -----------------------------------------------------
# Time Complexity: O(n)
# Space Complexity: O(1)
# Three different methods to perform linear search.
# =====================================================


# -----------------------------------------------------
# Method 1: Simple Loop Search (iterating values only)
# -----------------------------------------------------

my_list = [23, 54, 44, 32, 65]

def linearSearch(target):
    for item in my_list:
        if item == target:
            print(f"Element is present: {item}")
            return
    print("Element is not present")

linearSearch(32)



# -----------------------------------------------------
# Method 2: Using enumerate() to get index + value
# -----------------------------------------------------

my_list = [23, 54, 44, 32, 65]

def linearSearch(target):
    for idx, value in enumerate(my_list):
        if value == target:
            print(f"Element is present at index: {idx}")
            return
    print("Element is not present")

linearSearch(32)



# -----------------------------------------------------
# Method 3: Using range() and indexing
# -----------------------------------------------------

my_list = [23, 54, 44, 32, 65]

def linearSearch(target):
    for i in range(len(my_list)):
        if target == my_list[i]:
            print(f"Element is present at index: {i}, value: {my_list[i]}")
            return
    print("Element is not present")

linearSearch(32)
