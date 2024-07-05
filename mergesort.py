#Program to implememnt merge sort algorithm

lst=[45,98,23,12,4,101,87,67,50]

#Function that will merge sort the left and right list into a single list
def mergesort(left, right, lst):
    i=0; j=0; k=0;

    while(i<len(left) and j<len(right)):
        if left[i]<right[j]:
            lst[k]=left[i]
            i+=1
        else:
            lst[k]=right[j]
            j+=1
        k+=1

    while i<len(left):
        lst[k]=left[i]
        i+=1; k+=1

    while j<len(right):
        lst[k]=right[j]
        j+=1; k+=1

#Function to divide the list into equal parts left and right
def fun_div(lst):
    n=len(lst)
    if(n<2): #If the left or right list contains only one element the function must stop
        return

    mid=n//2
    left=[]
    right=[]

    for i in range(mid):
        left.append(lst[i])

    for i in range(mid,n):
        right.append(lst[i])

    fun_div(left)
    fun_div(right)

    mergesort(left, right, lst)

fun_div(lst)

for i in lst:
    print(i, end=' ')
print(lst)