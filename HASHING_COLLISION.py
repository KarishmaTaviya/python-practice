''' Python implememtation of hash table
Case-2: Assume that the hash algorithm / function returns DUPLICATE hash key'''

#celebrity_list=[(101,'Virat Kohli'),(108,'Anushka Sharma'),(111,'Ranveer Singh'),(119,'Deepika Padukone')]

#Function to create an empty hash table, assuming %10 as the hash algorithm
#Hence hash table must be an empty list with index from 0 to 9

def create_hash_table(n):       #n is the number of items in the list
    global hash_table
    hash_table =[[] for _ in range(n)]

create_hash_table(10)
print(hash_table)

#Function to insert / add key value pair to the hash table
def insert(hash_table,id,name):
    hash_bucket=id%10
    hash_table[hash_bucket].append((id, name))

insert(hash_table, 101, 'Virat Kohli')
insert(hash_table, 108, 'Anushka Sharma')
insert(hash_table, 111, 'Ranveer Singh')
insert(hash_table, 119, 'Deepika Padukone')

print(hash_table)

#Function to search from hash table
def search(item_list, id):
    hash_key = id%10
    for item in range(len(item_list)):
        if item == hash_key:
            for j in range(len(item_list[item])):
                if item_list[item][j][0]==id:
                    return item_list[item][j][1]

print('Searching 101: ',search(hash_table,101))

print('Searching 111: ',search(hash_table,111))
