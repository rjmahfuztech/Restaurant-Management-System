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