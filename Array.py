n  = [3,2,20,10,4,8,2,1]

minVal = n[0]

for i in n:
    if i < minVal:
        minVal = i

print(minVal)