# list get the player names from the user
# and also ask player to search from the list
# if available then also display the position of it

# player_list = input("Enter CSV : ").split(",")
# player_list = [i.lower() for i in player_list]
# player_name = input("Enter player name : ").lower()

# if player_name in player_list:
# 	print(player_name," is there in team")
# 	print(player_list.index(player_name)+1)
# else:
# 	print(player_name," is not there in team")



# l1 = [50,30,30,45,20]
# l2 = [20,34,40,15,30,20]

# print(l1,l2)

# s1=set(l1)
# s2=set(l2)

# s3 = s1.intersection(s2)
# print(list(s3))




# l1 = [11,20,13,24,55,6]
# print(max(l1),min(l1))
# l1.reverse()
# print(l1)

# l1.sort(reverse=True)
# print(l1)
# l1.clear()
# print(l1,len(l1))


# l1.pop(2)
# print(l1)
# l1.remove(20)
# print(l1)
# print(l1.count(200))

# l1.extend([20,30,40])
# print(l1)
# l1.insert(5,55)
# print(l1)
# l1.insert(0,5)
# print(l1)

# l1.append(50)
# print(l1)

# Cloning of the list
# l1 = [10,20,30,40,50]
# # l2 = l1[:] # cloning 
# l2 = l1.copy()
# print(l1,l2)
# print(id(l1),id(l2))
# l1[0] = 100
# print(l1,l2)
# l2[0] = 1000
# print(l1,l2)


# # alias
# l1 = [int(i) for i in input().split()]
# l2 = l1
# l1[0] = l1[0] + 5
# l2[0] = l2[0] + 5
# print(l1,l2)
# print(id(l1),id(l2))


# membership in list
# l1 = [int(i) for i in input().split()]
# n = int(input("Enter value to search: "))
# print(n not in l1)
# print(n in l1)


# Repetation of list
# l1 = [int(i) for i in input().split()]
# n = int(input("How many times to repeat? : "))
# print(l1*n)

# Concatenation
# l1 = [int(i) for i in input().split()]
# l2 = [int(i) for i in input().split()]

# print(l1+l2)