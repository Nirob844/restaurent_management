from foods.burger import Burger
from foods.drinks import Drinks
from foods.pizza import Pizza
from order.order import Order
from restaurant.restaurant import Restaurant
from users.chef import Chef
from users.customer import Customer
from users.manager import Manager
from users.server import Server


def main():
    # Create a restaurant
    my_restaurant = Restaurant("Gourmet Bistro", 2000)

    # Add menu items
    my_restaurant.menu.add_menu_item('pizza', Pizza("Margherita", 10.99, "Medium", ["Cheese", "Tomato"]))
    my_restaurant.menu.add_menu_item('burger', Burger("Cheeseburger", 8.99, "Beef", ["Lettuce", "Tomato", "Cheese"]))
    my_restaurant.menu.add_menu_item('drinks', Drinks("Coke", 1.99, True))
    my_restaurant.menu.add_menu_item('drinks', Drinks("Coffee", 2.99, False))

    # Add customers
    customer1 = Customer("Alice", "123-456-7890", "alice@example.com", "123 Maple St", 100)
    customer2 = Customer("Bob", "098-765-4321", "bob@example.com", "456 Oak St", 150)

    # Add employees
    chef1 = Chef("Gordon", "111-222-3333", "gordon@example.com", "789 Pine St", 5000, "2024-01-01", "Kitchen", "Italian")
    server1 = Server("John", "444-555-6666", "john@example.com", "321 Elm St", 3000, "2024-01-01", "Service")
    manager1 = Manager("Sarah", "777-888-9999", "sarah@example.com", "654 Birch St", 6000, "2024-01-01", "Management")

    my_restaurant.add_employee('chef', chef1)
    my_restaurant.add_employee('server', server1)
    my_restaurant.add_employee('manager', manager1)

    # Place orders
    order1 = Order(customer1, [my_restaurant.menu.items['pizza'][0], my_restaurant.menu.items['drinks'][0]])
    my_restaurant.add_order(order1)
    customer1.place_order(order1)

    order2 = Order(customer2, [my_restaurant.menu.items['burger'][0], my_restaurant.menu.items['drinks'][1]])
    my_restaurant.add_order(order2)
    customer2.place_order(order2)

    # Customers paying for their orders
    customer1.pay_for_order(20, my_restaurant)
    customer2.pay_for_order(15, my_restaurant)

    # Customers giving tips to the server
    customer1.give_tips(server1, 5)
    customer2.give_tips(server1, 3)

    # Show menu
    print(my_restaurant.show_menu())

    # Show orders
    print(my_restaurant.show_orders())

    # Show employees
    my_restaurant.show_employees()

if __name__ == "__main__":
    main()
