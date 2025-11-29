num  = [3,2,20,10,4,8,2,1]

temp = 0
n = len(num)
for i in range(n - 1):
    for j in range(n - i - 1):
        if num[j] > num[j + 1]:

            temp  = num[j]
            num[j] = num[j+1]
            num[j+1] = temp

print(num)
