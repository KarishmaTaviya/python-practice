#list manipulation

LST=[1,2,3,4]
NAME=['ABC','DEF']
print('LST : ',LST,'\nNAME : ',NAME)

#Add the list NAME to LST.
LST.append(NAME)
print('\nafter adding list NAME to list LST : ',LST)

#Add one more list [5,5] to LST at index value 2.
LST.insert(2,[5,5])
print('\nafter adding [5,5] to list LST : ',LST)
