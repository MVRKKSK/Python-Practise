class Employee:
    def __init__(self, name , age , salary , incentives):
        self.name = name 
        self.age = age 
        self.salary = salary
        self.incentives = incentives

    def total_salary(self):
        return self.salary + self.incentives

class SoftwareEmployee(Employee):
    def __init__(self, name, age, salary, incentives):
        self.name = name 
        self.age = age 
        self.salary = salary 
        self.incentives = incentives

    def total_salary(self):
        return self.salary+self.incentives


