rno = int(input("Enter Roll no: "))
name = input("Enter your name: ")
s1 = int(input("Mark of subject 1: "))
s2 = int(input("Mark of subject 2: "))
s3 = int(input("Mark of subject 3: "))
total = s1+s2+s3
per = total/3.0

print("*" * 40)
print("Marksheet")
print("%d  %s  %d  %d  %d  %d  %.2f"%(rno,name,s1,s2,s3,total,per))

print("*" * 40)