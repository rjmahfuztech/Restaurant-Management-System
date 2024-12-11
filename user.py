from abc import ABC

class User(ABC):
    def __init__(self,name,email,phone,address):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

class Employee(User):
    def __init__(self, name, email, phone, address,age,designation,salary):
        super().__init__(name, email, phone, address)
        self.age = age
        self.designation = designation
        self.salary = salary

class Admin(User):
    def __init__(self,name,email,phone,address):
        super().__init__(name,email,phone,address)
        self.employees = []

    def add_employee(self,name,email,phone,address,age,designation,salary):
        employee = Employee(name,email,phone,address,age,designation,salary)
        self.employees.append(employee)
        print(f'Added an employee, name = {name}')

    def view_employee(self):
        for emp in self.employees:
            print(emp.name,emp.age,emp.address,emp.email)


user = Admin('Mahfuz','mahfuz@gmail.com',2044839,'Rajshahi')
user.add_employee('rohim','rohim@gmail.com',99548,'Tanor',19,'player',50002)
user.add_employee('sakib','rohim@gmail.com',99548,'Tanor',15,'player',50002)
user.add_employee('rakib','rohim@gmail.com',99548,'Tanor',23,'player',50002)

user.view_employee()