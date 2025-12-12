# Our unsorted array
my_array = [64, 34, 25, 5, 22, 11, 90, 12]

# Get the number of elements in the array
n = len(my_array)

# Outer loop: goes from index 0 to n-2
# (Because the last element will already be sorted)
for i in range(n - 1):

    # Assume the smallest element is at index i
    min_index = i

    # Inner loop: look at all elements to the RIGHT of i
    for j in range(i + 1, n):

        # If we find a smaller value than the current minimum,
        # update min_index
        if my_array[j] < my_array[min_index]:
            min_index = j

    # Remove the smallest value from its old position
    min_value = my_array.pop(min_index)

    # Insert it into the correct position (index i)
    my_array.insert(i, min_value)

# Print the sorted array
print("Sorted array:", my_array)


# the above algorithm has many shifting operation so we improve 





array = [10,3,9,2,49,29,30,1,5,90]

n = len(array)
temp = 0
for i in range(n-1):
    min_value = i

    for j in range(i+1 , n):
        if array[j] < array[min_value]:
            min_value = j
    temp = array[i]
    array[i] = array[min_value]
    array[min_value] = temp

print("Sorted array : "  , array)  