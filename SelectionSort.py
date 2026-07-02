num =[64, 34, 25, 5, 22, 11, 90, 12]
n = len(num)
for i in range(n-1):
    min_idx = i
    for j in range(i+1,n):
        if num[j]< num [min_idx]:
            min_idx = j
    min_value = num.pop(min_idx )
    num.insert(i,min_value)
print(num)
