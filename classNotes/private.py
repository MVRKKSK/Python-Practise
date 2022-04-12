class Person:
    def __init__(self , name , age , salary):
        self.name = name
        self.age = age
        self.__salary = salary
    def show(self):
        print(f'Name : {self.name}  age : {self.age}  salary : {self.__salary}')
class Employee(Person):
    def __init__(self, name, age, __salary , bonus):
        super().__init__(name , age ,__salary)
        self.bonus = bonus

e1 = Employee("kautilya", 19, 50 , 1)

e1.show()