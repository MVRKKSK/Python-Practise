class Student:
    def __init__(self , name , registration_no , total_marks):
        self.name = name
        self.registration_no = registration_no
        self.total_marks = total_marks

    def show(self):
        print("name: ",self.name , "Registration No: " , self.registration_no , "Total Marks: " , total_marks)

n = int(input("enter no of students: "))
name =" "
registration_no = " "
total_marks = " "
for i in range(n):
    name = input("enter your name: ")
    registration_no = input("enter your registration no: ")
    total_marks = input("enter your total marks: ")

    s1 = Student(name, registration_no, total_marks)
    s1.show()
