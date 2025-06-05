dict1 = {"ankit":98,"akash":97,"aryan":86,"robin":94}
def student_call():
    student_name= str(input("enter student's name:"))
    student_name1=student_name.lower()
    if (student_name1 in dict1) == True:
        print(student_name+"'s marks:",dict1[student_name1])
    else:
        print("student not found")

student_call()
