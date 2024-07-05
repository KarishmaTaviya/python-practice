def binary_search(search_list,s):
	first = 0
	last = len(search_list)-1
	found = False
	while( first<=last and not found):
		mid = (first + last)//2
		if search_list[mid] == s :
			found = True
		else:
			if s < search_list[mid]:
				last = mid - 1
			else:
				first = mid + 1	
	return found
	
print(binary_search([1,2,3,5,8], 6))
print(binary_search([1,2,3,5,8], 5))


