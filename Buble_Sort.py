# Our unsorted list
num = [3, 2, 20, 10, 4, 8, 2, 1]

# A temporary variable to help with swapping
temp = 0

# Length of the list
n = len(num)

# Outer loop: runs n-1 times
# Each loop will push the largest unsorted value to the end
for i in range(n - 1):

    # Inner loop: compares adjacent elements
    # We use (n - i - 1) because after every full pass,
    # the last i elements are already sorted
    for j in range(n - i - 1):

        # Compare two adjacent numbers
        if num[j] > num[j + 1]:

            # Swap them if they are in the wrong order
            temp = num[j]          # store value of num[j]
            num[j] = num[j + 1]    # move smaller value forward
            num[j + 1] = temp      # put larger value behind

# Print the sorted list
print(num)
