# from abc import ABC

# class User(ABC):
#     def __init__(self,name,email,phone,address):
#         self.name = name
#         self.email = email
#         self.phone = phone
#         self.address = address

# class Customer(User):
#     def __init__(self, name, email, phone, address):
#         super().__init__(name, email, phone, address)
#         self.cart = Order()

#     def view_menu(self,restaurant):
#         restaurant.menu.show_menu_item()
        
#     def add_to_cart(self,restaurant,item_name,quantity):
#         item = restaurant.menu.find_item(item_name)
#         if item:
#             if item.quantity < quantity:
#                 print(f'Sorry!! Quantity limit exceeded, available: {item.quantity}, but you want: {quantity}')
#             else:
#                 item.quantity = quantity
#                 self.cart.add_item(item)
#                 print('Item added')
#         else:
#             print('Item not found!!!')
        
#     def view_cart(self):
#         print('****View Cart****')
#         print('Name\tPrice\tQuantity')
#         for item, quantity in self.cart.items.items():
#             print(f'{item.name}\t{item.price}\t{quantity}')
#         print(f"Total Price: {self.cart.total_price}")

        
# class Order:
#     def __init__(self):
#         self.items = {}

#     def add_item(self,item):
#         if item in self.items:
#             self.items[item] += item.quantity # Jodi item ta cart a already thaka
#         else:
#             self.items[item] = item.quantity # Jodi item cart a na thaka
    
#     def remove(self,item):
#         if item in self.items:
#             del self.items[item]
    
#     @property
#     def total_price(self):
#         return sum(item.price * quantity for item,quantity in self.items.items())
    
#     def clear(self):
#             self.items = {}

# class Employee(User):
#     def __init__(self, name, email, phone, address,age,designation,salary):
#         super().__init__(name, email, phone, address)
#         self.age = age
#         self.designation = designation
#         self.salary = salary

# class Admin(User):
#     def __init__(self,name,email,phone,address):
#         super().__init__(name,email,phone,address)
#         # self.employees = []

#     # CONFUSED HERE!!!!!!!!!!!! 
#     # def add_employee(self,name,email,phone,address,age,designation,salary):
#     #     employee = Employee(name,email,phone,address,age,designation,salary)
#     #     self.employees.append(employee)
#     #     print(f'Added an employee, name = {name}')
#     def add_employee(self,restaurant,employee):
#         restaurant.add_employee(employee)

#     # def view_employee(self):
#     #     for emp in self.employees:
#     #         print(emp.name,emp.age,emp.address,emp.email)
#     def view_employee(self,restaurant):
#         restaurant.view_employee()

#     def add_new_item(self,restaurant,item):
#         restaurant.menu.add_menu_item(item)
    
#     def remove_item(self,restaurant,item):
#         restaurant.menu.remove_item(item)


# class Restaurant:
#     def __init__(self,name):
#         self.name = name
#         self.employees = [] # Employee Database
#         self.menu = Menu()
    
#     def add_employee(self,employee):
#         self.employees.append(employee)

#     def view_employee(self):
#         print('Employee List:')
#         for emp in self.employees:
#             print(emp.name,emp.age,emp.address,emp.email)

# class Menu:
#     def __init__(self):
#         self.items = [] # Product Database

#     def add_menu_item(self,item):
#         self.items.append(item)
    
#     def find_item(self,item_name):
#         for item in self.items:
#             if item.name.lower() == item_name.lower():
#                 return item
#         return None
    
#     def remove_item(self,item_name):
#         item = self.find_item(item_name)
#         if item:
#             print(f'Item ({item_name})  is deleted')
#             self.items.remove(item)
#         else:
#             print(f'Item ({item_name}) not found')
    
#     def show_menu_item(self):
#         print('*****Menu*****')
#         print('Name\tPrice\tQuantity')
#         for item in self.items:
#             print(f'{item.name}\t{item.price}\t{item.quantity}')

# class FoodItem:
#     def __init__(self,name,price,quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity

# # user = Admin('Mahfuz','mahfuz@gmail.com',2044839,'Rajshahi')
# # user.add_employee('rohim','rohim@gmail.com',99548,'Tanor',19,'player',50002)
# # user.add_employee('sakib','rohim@gmail.com',99548,'Tanor',15,'player',50002)
# # user.add_employee('rakib','rohim@gmail.com',99548,'Tanor',23,'player',50002)
# # user.view_employee()


# my_res = Restaurant('My Restaurant')
# mn = Menu()
# item = FoodItem('banana',12,16)
# item2 = FoodItem('Apple',4,8)
# item3 = FoodItem('Guava',16,24)
# admin = Admin('Mahfuz','mahfuz@gmail.com',204848,'Rajshahi')
# admin.add_new_item(my_res,item)
# admin.add_new_item(my_res,item2)
# admin.add_new_item(my_res,item3)

# customer1 = Customer('Mahfuz','mahfuz@gmail.com',204848,'Rajshahi')
# customer1.view_menu(my_res)

# item = input('Enter item name: ')
# item_quantity = int(input('Enter item quantity: '))
# customer1.add_to_cart(my_res,item, item_quantity)
# customer1.view_cart()