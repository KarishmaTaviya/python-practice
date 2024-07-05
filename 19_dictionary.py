#dictionary

num_students = int(input("Please enter number of students : "))
#print ("you entered students : ", num_students)
STUDENT = {}
student_data = ['Name ', 'Contact ', 'Email ','Address ']

for i in range(0,num_students):
    student_id = input("ID :")
    STUDENT[student_id] = {}
    for entry in student_data:
        STUDENT[student_id][entry] = input(entry) #storing data

print('Student Info :\n',STUDENT)
'''
#print student info
ID = input("Student ID : ")

if ID in STUDENT.keys():
    print ("Student Info: \n", STUDENT[ID].values())
else:
    print("please enter valid ID")
'''
