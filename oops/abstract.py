class Employee :
    def __init__(self , name , salary , age):
        self.name = name
        self.salary = salary
        self.age = age
    
    def __str__(self):
        return("{0} , {1} , {2}").format(self.name , self.salary , self.age)

    def getSalary(self):
        return self.salary

    def __compare__(self,other):
        if(self.salary < other.salary):
            return other
        else:
             return self

e1 = Employee("kautilya", 6000 , "19")
e2 = Employee("akashi", 3000 , "19")

print(e1.__compare__(e2))
