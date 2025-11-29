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