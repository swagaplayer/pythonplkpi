lst = [0,1,2,3,4]
for i in range (0,len(lst)-1):
    if lst[i] == 0:
        lst.remove(lst[i])
print(lst)
