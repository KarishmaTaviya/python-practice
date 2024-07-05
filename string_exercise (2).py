# 1) wpp that will ask user to provide password. print valid/invalid password
# based on below rules,
# -> lenght should be greater than or equal to 10
# -> should have at least 1 digit
# -> it should contain 1 uppercase and 1 lowercase letter
# -> it should contain 1 special symbol

# s = input("Enter password : ")
# alpha = 0
# num = 0
# upper = 0
# lower = 0
# ss = 1
# space = 0
# if(len(s) >= 10):
# 	for i in s:
# 		if(i.isdigit()):
# 			num = 1
# 		if(i.isalpha()):
# 			alpha = 1
# 		if(not i.isalnum()):
# 			ss = 0
# 		if(i.isupper()):
# 			upper = 1
# 		if(i.islower()):
# 			lower = 1
# 		if(i.isspace()):
# 			space = 1
# 	if(upper==1 and lower==1 and ss==0 and alpha==1 and num==1 and space==0):
# 		print("valid")
# 	else:
# 		print("Invalid")
# else:
# 	print("Ivalid Password")




# 2) most wanted letter
# you are given text which contain diff english letters and symbols
# you have to find the frequent letter in the text with below rule

# 1-> letter returned must be in lowercase
# 2-> case doesnt matter
# 3-> do not count punctuation symbols, digits, and spaces
# 4-> if two or more letters have same frequency then return the letter
#  	which comes first in alphabet

# s = input("Enter text : ").lower()
# ss = ""
# max = 0
# op = ""
# for i in s:
# 	if(i.isalpha()):
# 		ss = ss + i
# ss = list(ss)
# print(ss)
# ss.sort()

# for i in range(0,len(ss)):
# 	if(s.count(ss[i])>max):
# 		max = s.count(ss[i])
# 		op = ss[i]
# print("Frequency of ", op , "is ",max)


# 3) wpp to count all letters, digits and special symbol, from given string

# s = input("Enter text : ")
# alpha = 0
# dig = 0
# ss = 0
# for i in s:
# 	if(i.isalpha()):
# 		alpha += 1
# 	if(i.isdigit()):
# 		dig += 1
# 	if(not i.isalnum() and not i.isspace()):
# 		ss += 1
# print("Letters : ",alpha)
# print("Digits : ",dig)
# print("Special Symbol : ",ss)




# 4)wpp to find all occurence of sub string in given string by ignoring case

# s = input("Enter String : ").lower()
# ss = input("Enter Substring : ").lower()

# n = s.find(ss)
# while(n!=-1):
# 	print(n)
# 	n = s.find(ss,n+1,len(s))



# 5)calculate sum & avg of digits present in string

# s = input("Enter String : ")
# sum = 0
# avg = 0
# count = 0
# for i in s:
# 	if i.isdigit():
# 		sum += int(i)
# 		count += 1
# avg = sum / count
# print("No of digits in String : ",count)
# print("Sum of digits in String : ",sum)
# print("Avg of digits in String : ",avg)




# 6) split a string on hyphens
	
# s = input("Enter String : ")

# ss = s.split("-")
# print(ss)

# 7) replace each spcial symbol with star in the string

# s = input("Enter String : ")
# ss = ""
# for i in s:
# 	if (not i.isalnum() and not i.isspace()):
# 		ss += "*"
# 	else:
# 		ss += i
# print(ss)


# 8) check whether string is symmetrical and palindrome

# s = input("Enter String : ")
# l = len(s)

# if(s[0:l//2]==s[l//2:] and s == s[::-1]):
# 	print(s,"is symmetrical and palindrome")
# else:
# 	print(s,"is niether symmetrical nor palindrome")



# s = input("Enter String : ")
# l = len(s)
# sym = 1
# plndrm = 1
# if(l%2 != 0):
# 	sym = 0
# for i in range(0,l//2):
# 	if(s[i] != s[i + l//2]):
# 		sym = 0
# 	if(s[i] != s[l - i - 1]):
# 		plndrm = 0
# if(sym == 1 and plndrm == 1):
# 	print(s,"is symmetrical and palindrome")
# elif(sym == 1 and plndrm == 0):
# 	print(s,"is symmetrical but not palindrome")
# elif(sym == 0 and plndrm == 1):
# 	print(s,"is palindrome but not symmetrical")
# else:
# 	print(s,"is niether symmetrical nor palindrome")





# 9) remove all duplicate characters from string

# s1 = input("Enter String : ")
# s2 = ""
# for i in range(0,len(s1)):
# 	if(s1[i] not in s2):
# 		s2 += s1[i]
# print(s2)

# 10) wpp to get number from user and print it in alphabatic form

# n = int(input("Enter Number : "))


# 11) determine iif word or phrase is isogram (no repeating letter, space and hyphen are allowed)

# s1 = input("Enter String : ")
# s2 = ""
# for i in s1:
# 	if(i.isspace() or i.isalpha() or i == "-"):
# 		if(i not in s2 or i.isspace() or i == "-"):
# 			s2 += i
# if(s1 == s2):
# 	print("isogram")
# else:
# 	print("not isogram")


 # 12)  "what is 5 plus 2?" answer should be 7  

s = input("Enter Question [your question should be like \"what is 5 plus 2?\"] : ")
l = s.split(" ")
print(l)
args1 = int(l[2])
args2 = l[4]
args2 = int(args2[0:len(args2)-1])

print(args1,args2)

