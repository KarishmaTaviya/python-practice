''' Python implememtation of hash table
Case-1: Assume that the hash algorithm / function returns unique hash key'''

#celebrity_list=[(101,'Virat Kohli'),(108,'Anushka Sharma'),(111,'Ranveer Singh'),(119,'Deepika Padukone')]

#Function to create an empty hash table, assuming %17 as the hash algorithm
#Hence hash table must be an empty list with index from 0 to 16

def create_hash_table(n):       #n is the number of items in the list
    global hash_table
    hash_table =[(None,None)]*n

create_hash_table(17)
print(hash_table)   #to check if an empty hash table is created or not

#Function to insert / add key value pair to the hash table
def insert(hash_table,id,name):
    hash_key=id%17
    hash_table[hash_key]=(id,name)

#Function to search from hash table
def search(item_list, id):
    hash_key = id%17
    for item in range(len(item_list)):
        if item==hash_key:
            return item_list[item][1]

insert(hash_table, 101, 'Virat Kohli')
insert(hash_table, 108, 'Anushka Sharma')
insert(hash_table, 111, 'Ranveer Singh')
insert(hash_table, 119, 'Deepika Padukone')

print(hash_table)

print('Searching 101: ',search(hash_table,101))

print('Searching 119: ',search(hash_table,119))

