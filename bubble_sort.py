lst=[12,4,9,34,87,5]

for i in range(len(lst)):
    for j in range(len(lst)-i-1):
        if lst[j]>lst[j+1]:
            temp=lst[j+1]
            lst[j+1]=lst[j]
            lst[j]=temp

print('List : ', lst)


def bubsort(lst):
    for i in range(len(lst)):
        for j in range(len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                temp = lst[j + 1]
                lst[j + 1] = lst[j]
                lst[j] = temp
    return lst

lst=bubsort([5,4,3,2,1])
print('List : ',lst)
