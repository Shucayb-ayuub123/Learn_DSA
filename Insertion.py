# Our unsorted array
my_array = [64, 34, 25, 12, 22, 11, 90, 5]

# Get the length of the array
n = len(my_array)

# Loop from index 1 to n-1 (because the first element is already "sorted")
for i in range(1, n):

    # Assume the current index is where the element will be inserted
    insert_index = i

    # Remove the element at index i (the one we want to insert in correct place)
    current_value = my_array.pop(i)

    # Loop backwards from i-1 down to 0
    for j in range(i - 1, -1, -1):

        # If an element is bigger than the current_value,
        # we move insert_index to that position (meaning current_value should be inserted before it)
        if my_array[j] > current_value:
            insert_index = j

    # Insert current_value into the correct sorted position
    my_array.insert(insert_index, current_value)

# Print the sorted array
print("Sorted array:", my_array)




# the above algorith has many shifting operation so we improve 

array = [10,3,9,2,49,29,30,1,5,90]

# n = len(array)
# for i in range(1,n):
#     insert_index = i
#     current_value = array[i]
#     for j in range(i-1, -1, -1):
#         if array[j] > current_value:
#             array[j+1] = array[j]
#             insert_index = j
#         else:
#             break
#     array[insert_index] = current_value
# print("Sorted array:", array)

