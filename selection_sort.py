lst=[12,4,9,34,87,5]

for i in range(len(lst)):
    temp=lst[i]
    ind=i
    for j in range(i+1,len(lst)):
        if lst[j]<temp:
            temp=lst[j]
            ind=j

    lst[ind] = lst[i]
    lst[i]=temp
print(lst)
