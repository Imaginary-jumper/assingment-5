from operator import truediv

n= int(input("how many studetns data you want to enter:"))
dict1 = {}
for i in range (n):
    a= str(input("enter sno.{} studetn's name:".format(i+1)))
    b= int(input("enter sno.{} student's marks:".format(i+1)))
    dict1[a]=b
print("your dictionary have been created successfully")

def student_call():
    student_name= str(input("enter student's name:"))
    if (student_name in dict1) == True:
        print(student_name+"'s marks:",dict1[student_name])
    else:
        print("student not found")

student_call()


