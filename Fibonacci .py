prev1=1
prev2=0

print(prev1)
print(prev2)

for fibo in range(18):
    new_fibo = prev1 + prev2
    print(new_fibo)
    prev1 = prev2
    prev2 = new_fibo
