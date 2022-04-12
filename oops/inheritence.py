class exam:
    def __init__(self , name , id , marks , friends):
         self.id = id
         self.marks = marks
         self.name = name
         self.friends = friends

    def show(self):
        print("ID", self.id , "marks: " , self.marks , "name" , self.name , "friends" , self.friends)

class Student(exam):
    pass
s1 = Student("kautilya", "55444", "56", "suryamani")
s1.show()

