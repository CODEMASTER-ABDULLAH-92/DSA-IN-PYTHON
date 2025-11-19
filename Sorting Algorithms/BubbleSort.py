# =====================================================
# BUBBLE SORT IN PYTHON
# -----------------------------------------------------
# Time Complexity: O(n²)
# Space Complexity: O(1)
# Idea:
#   - Repeatedly compare adjacent elements
#   - Swap them if they are in the wrong order
#   - Largest elements bubble to the end
# =====================================================

my_list = [23, 54, 44, 32, 65]

def bubbleSort(length):
    # Outer loop → number of passes
    for i in range(length - 1):
        # Inner loop → compare adjacent elements
                # range(start, stop)
        for j in range(0, length - 1 - i):
            if my_list[j] > my_list[j + 1]:  # if out of order
                # Swap
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]

    return my_list  # return sorted list


# Output
print("Sorted List:", bubbleSort(len(my_list)))