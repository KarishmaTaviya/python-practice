
n = int(input("Enter n = "))
for i in range(1,n+1,2):
	print("---"*((n-i)//2),end="")
	print(".|."*i,end="")
	print("---"*((n-i)//2))
z = n * 3 - 8
print("-"*(z//2),end="")
print("WELOCOME",end="")
print("-"*(z-z//2))
for i in range(n,0,-2):
	print("---"*((n-i)//2),end="")
	print(".|."*i,end="")
	print("---"*((n-i)//2))

#   1
#   3   2
#   6   5   4
#  10   9   8   7

# n = int(input("Enter n = "))
# k = 0
# for i in range(1,n):
# 	for j in range(i,0,-1):
# 		print("%3d "%(j+k),end="")
# 	k = i+k
# 	print()

# 1
# 2 3
# 4 5 6
# 7 8 9 10
# n = int(input("Enter n = "))
# k = 1
# for i in range(1,n+1):
# 	for j in range(1,i+1):
# 		print("%d "%k,end="")
# 		k += 1
# 	print()


# #     *
# #   *   *
# # *       *
# #   *   *
# #     *
# n = int(input("Enter n = "))
# for i in range(1,n+1,2):
# 	print(" "*(n-i),end="")
# 	for j in range(1,i+1):
# 		if(j==1 or j==i ):
# 			print("* ",end="")
# 		else:
# 			print("  ",end="")
# 	print()

# for i in range(n-2,0,-2):
# 	print(" "*(n-i),end="")
# 	for j in range(1,i+1):
# 		if(j==1 or j==i ):
# 			print("* ",end="")
# 		else:
# 			print("  ",end="")
# 	print()

#     *
#   * * *
# * * * * *
#   * * *
#     *
# n = int(input("Enter n = "))
# for i in range(1,n+1,2):
# 	print(" "*(n-i),end="")
# 	print("* "*i)
# for i in range(n-2,0,-2):
# 	print(" "*(n-i),end="")
# 	print("* "*i)


#  * * * *
#    * * *
#      * *
#        *
# n = int(input("Enter n = "))
# for i in range(n,0,-1):
# 	print("  "*(n-i),end="")
# 	print("* "*i)


# * * * *
# * * *
# * *
# *
# n = int(input("Enter n = "))
# for i in range(n,0,-1):
# 	print("* "*i)