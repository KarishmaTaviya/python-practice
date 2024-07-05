def binary_search(search_list,s,first,last):
    if last>=first:
        mid=first+(last-first)
        if search_list[mid]==s:
            return mid
        elif search_list[mid]>s:
            return binary_search(search_list,s,first,mid-1)
        else:
            return binary_search(search_list,s,mid+1,last)
    else:
        return -1

search_list=[1,2,3,5,8]
s=5
result=binary_search(search_list,s,0,len(search_list)-1)
print(result)
if (result!=-1):
    print("found")
else:
    print("not found")
            
