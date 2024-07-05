lst=[12,4,7,6,78,8]
#lst=[12,4,9,34,87,5]

for i in range(1,len(lst)):
    temp=lst[i]
    j = i - 1
    while(temp<lst[j] and j>=0):
        lst[j+1]=lst[j]
        j=j-1
    lst[j+1] = temp
print(lst)
