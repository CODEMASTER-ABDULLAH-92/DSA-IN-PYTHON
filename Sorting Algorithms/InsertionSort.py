my_list = [23, 54, 44, 32, 65]

def insertionSort(length):
    # Loop starts from index 1 because index 0 is already "sorted"
    for i in range(1, length):

        # j moves backward to compare elements behind the current element
        for j in range(i, 0, -1):

            # If the left element is greater than the right element → swap
            if my_list[j - 1] > my_list[j]:
                my_list[j], my_list[j - 1] = my_list[j - 1], my_list[j]
            else:
                # If the correct position is found, stop checking backward
                break

    return my_list

print(insertionSort(len(my_list)))
