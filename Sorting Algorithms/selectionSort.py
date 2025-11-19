# =====================================================
# SELECTION SORT IN PYTHON
# -----------------------------------------------------
# Time Complexity: O(n²)
# Space Complexity: O(1)
# Idea:
#   - Find the minimum element in the unsorted part
#   - Swap it with the element at the current index
#   - Repeat for all positions
# =====================================================

my_list = [23, 54, 44, 32, 65]

def selectionSort(length):
    
    # Loop over each index of the list
    for i in range(length):
        
        # Assume the current index is the minimum
        minIndex = i
        
        # Search for a smaller value in the remaining list
        for j in range(i + 1, length):
            if my_list[j] < my_list[minIndex]:
                minIndex = j   # Update the index of the new minimum
        
        # Swap only if the minimum is NOT the current element
        my_list[i], my_list[minIndex] = my_list[minIndex], my_list[i]
    
    # Return the sorted list
    return my_list


# Print the sorted list
print("Sorted List:", selectionSort(len(my_list)))
