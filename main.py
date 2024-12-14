from food_item import FoodItem
from menu import Menu
from order import Order
from restaurant import Restaurant
from users import Customer,Employee,Admin

boos_restaurant = Restaurant("Boos VIP Restaurant")

def customer_menu():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone: ")
    address = input("Enter your address: ")
    customer = Customer(name=name,email=email,phone=phone,address=address)

    while True:
        print(f'Welcome {customer.name}!!')
        print("1. View Menu")
        print("2. Add item to cart")
        print("3. View cart")
        print("4. Pay bill")
        print("5. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            customer.view_menu(boos_restaurant)
        elif choice == 2:
            item_name = input("Enter item name: ")
            item_Quantity = int(input("Enter item Quantity: "))
            customer.add_to_cart(boos_restaurant,item_name,item_Quantity)
        elif choice == 3:
            customer.view_cart()
        elif choice == 4:
            customer.pay_bill()
        elif choice == 5:
            break
        else:
            print("Invalid Input!!!!!!")

def admin_menu():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone: ")
    address = input("Enter your address: ")
    admin = Admin(name=name,email=email,phone=phone,address=address)

    while True:
        print(f'Welcome {admin.name}!!')
        print("1. Add new item")
        print("2. Add new employee")
        print("3. View employees")
        print("4. View items")
        print("5. Delete item")
        print("6. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            item_name = input("Enter item name: ")
            item_price = int(input("Enter item price: "))
            item_quantity = int(input("Enter item quantity: "))
            item = FoodItem(item_name,item_price,item_quantity)
            admin.add_new_item(boos_restaurant,item)
        elif choice == 2:
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            phone = input("Enter your phone: ")
            address = input("Enter your address: ")
            age = int(input("Enter your age: "))
            designation = input("Enter your designation: ")
            salary = int(input("Enter your salary: "))
            new_emp = Employee(name,email,phone,address,age,designation,salary)
            admin.add_employee(boos_restaurant,new_emp)
        elif choice == 3:
            admin.view_employee(boos_restaurant)
        elif choice == 4:
            admin.view_items(boos_restaurant)
        elif choice == 5:
            item_name = input("Enter item name: ")
            admin.remove_item(boos_restaurant,item_name)
        elif choice == 6:
            break
        else:
            print("Invalid Input!!!!!!")

while True:
    print(f"Welcome to the {boos_restaurant.name}!!")
    print("1. Admin")
    print("2. Customer")
    print("3. Exit")
    option = int(input("Enter your choice: "))
    if option == 1:
        admin_menu()
    elif option == 2:
        customer_menu()
    elif option == 3:
        break
    else:
        print("Sorry!! Invalid Choice!")