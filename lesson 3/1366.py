lst = [10, 5, 8, 12, 3, 15, 6, 9, 11, 7, 14, -1, 13, 4, 1]
sum = 0
for i in range(len(lst)):
    if i %2 !=0:
        sum += lst[i]
print(sum)