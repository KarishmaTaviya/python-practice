# 1) wpp to create dict like {1:1,2:4,3:9} (user input)

# n = int(input("Enter n = "))
# d = {}
# for i in range(1,n+1):
# 	d[i] = i**2
# print(d)


# 2) wpp to merge two dicts 

# d1 = {1:"abc",2:"def",3:"ghi"}
# d2 = {4:"jkl",5:"mno"}
# d1.update(d2)
# print(d1)


# 3) wpp to total of values in the dict 

# d = {"Pen":40,"Pencil":50,"Scale":60}
# print(sum(d.values()))


# 4) make stationary dict and find out costliest and cheapest item (10 items in dict)

# d = {"Pen":40,"Pencil":50,"Scale":60,"Eraser":5,"Lead Box":20,"Book":100,"Compass Box":120,"Sharpner":4,"Stapler":50,"Parker Pen":500}
# vmax = max(d.values())
# vmin = min(d.values())
# for k,v in d.items():
# 	if(vmax == v):
# 		print("Costliest item is : ",k)
# 	if(vmin == v):
# 		print("Cheapest item is : ",k)




# 5) print all unique value from dict

# d = {"Pen":40,"Pencil":50,"Scale":60,"Eraser":50,"Lead Box":120,"Book":100,"Compass Box":120,"Sharpner":40,"Stapler":50,"Parker Pen":500}
# dl = d.values()
# print(set(dl))
# l = []
# for i in dl:
# 	l += [i]
# for i in l:
# 	if(l.count(i) == 1):
# 		print(i,end=" ")

# 6) wpp make dict like {1:['a','b'],2:['c','d']} and output should be "ac ad bc bd"

# d = {1:['a','b'],2:['c','d']}
# l1,l2 = [i for i in d.values()]
# for i in l1:
# 	for j in l2:
# 		print(i+j)


# 7) wpp to print dict in table format




# 8) input is [('yellow',70),('Red',80),('Red',90),('yellow',60)]
# 	output should be {"yellow":[70,60],"Red":[80,90]}

loft = [('Yellow',70),('Red',80),('Red',90),('Yellow',60)]
d = {}
l = []
for i in loft:
	d.update({i[0]:i[1]})

# 9) input [{"python":[1,2,3,4,5]},{"java":[3,4,8,6,7]}]
# 	output should be [{"python":1,"java":3},{"python":2,"java":4},...]

  