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

emp = Employee('mahfuz','mah@gmail.com',39493,'Baya,Rajshahi',22,'Student',1000)

print(emp.address)
# class Admin(User):
#     def __init__(self,name,email,phone,address):
#         super().__init__(name,email,phone,address)
#         self.employees = []

#     def add_employee()