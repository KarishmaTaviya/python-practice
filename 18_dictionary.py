#Dictionary

MonstaX = {'1':'Shownu','2':'Wonho','3':'Minhyuk','4':'Kihyun','5':'Hyungwon','6':'Joohoney','7':'I.M.','MonstaX':'OT7'}

print('Dictionary is :\n',MonstaX)

print('\nThe length of the dictionary - MonstaX - is : ',len(MonstaX))

#cpoy()
monsta=MonstaX.copy()
print('\nmonsta from MonstaX is : ',monsta)

#get()
print('\nThe get() method gets value of the key specified : ',MonstaX.get('2'))

#items()
print('\nAll the items of the dictionary are : ',MonstaX.items())

#keys()
print('\nAll the keys of the dictionary are : ',MonstaX.keys())

#values()
print('\nAll the values of the dictionary are : ',MonstaX.values())

#pop()
print('\nRemoving the item at key 5 : ',monsta.pop('5'))

#popitem()
print('\nRemoving first element : ',monsta.popitem())

#setdefault()
print('\nSetdefault method : ',monsta.setdefault('MX','OT7'))

#update()
monsta.update(MonstaX='I am what I am')
print('\nUpdate method : ',monsta)

monsta.clear()
print('\nAll the items cleared in the dictionary : ',monsta)

