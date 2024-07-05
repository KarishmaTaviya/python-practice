#uses of list

#Create a list LST with 5 numbers [20, 5, 15,10,25]
LST=[20,5,15,10,25]

#Print the list using for loop.
print('List is as follows:')
for i in LST:
    print(i)

#Display the first three elements of the list.
print('\nFirst three elements are : ',LST[0:3])

#Display the last element of the list using negative index.
print('\nLast element is : ',LST[-1])

#Add 5 at the end of the list.
LST.append(5)
print('\nafter adding 5 at the end : ',LST)

#Add 44 at index value 3 in the list.
LST.insert(3,44)
print('\nafter adding 44 at 3rd index : ',LST)

#Add 5,31 and 30 to the list.
LST.extend((5,31,30))
print('\nafter adding 5,31,30 : ',LST)

#Remove the last number 30 from the list.
LST.pop()
print('\nafter removing the last value : ',LST)

#Remove the number from index value 7.
LST.pop(7)
print('\nafter removing the value at 7th index : ',LST)

#Create LST1 that is a copy of LST.
LST1=LST.copy()
print('\nnew list from existing list - LST1 : ',LST1)

#Check the id of LST & LST1.
print('\nIDs of both the lists :\nLST : ',id(LST),'\nLST1 : ',id(LST1))

#Count how many times the number 5 is getting repeated in the list.
print('\nthe value 5 is repeated ',LST.count(5),' times')

#Arrange the numbers of the list LST in ascending order.
LST.sort()
print('\nlist LST in ascending order : ',LST)

#Arrange the numbers of the list LST1 in descending order.
LST1.sort(reverse=True)
print('\nlist LST1 in descending order : ',LST1)

#Using a single method remove all elements from LST1.
LST1.clear()
print('\nlist after removing all the values',LST1)

#Delete the list LST.
del LST
print('list LST is deleted')
