num = [2,7,15,8,9]
n = len(num)
for i in range ( n-1):
    for j in range (n-i-1):
        if num[j] > num[j+1]:
            num[j], num[j+1] = num[j+1], num[j]
print(num)