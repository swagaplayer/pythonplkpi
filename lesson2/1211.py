lst = [1,2,3,4,5,6,7,8]
avg = sum(lst)/len(lst)
count = 0
for x in lst:
    if x > avg:
        count += 1
print(count)