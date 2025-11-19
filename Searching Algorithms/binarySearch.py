# Binary Search in Python
# ------------------------
# Works only on a sorted list.
# Time Complexity: O(log n)
# Space Complexity: O(1)

my_list = [23, 32, 44, 54, 65]

def binarySearch(target, length):
    # Initialize start and end pointers
    start = 0
    end = length - 1

    # Loop until the search space is valid
    while start <= end:

        # Calculate the middle index (avoids integer overflow)
        mid = start + (end - start) // 2

        # Check if the target is found
        if my_list[mid] == target:
            return mid   # Return index where target is found

        # If target is greater, ignore left half
        elif my_list[mid] < target:
            start = mid + 1

        # If target is smaller, ignore right half
        else:
            end = mid - 1

    # If the loop ends, target is not found
    return -1

# Call the function
value = binarySearch(32, len(my_list))

# Print the result
print("Element found at index:", value)
