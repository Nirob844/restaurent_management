# Restaurant Management System

This project is a Restaurant Management System implemented in Python, using object-oriented programming principles. It allows for managing customers, employees, menu items, orders, and finances of a restaurant.

## Project Structure

The project is organized into several modules:

- **users/**: Contains classes for different types of users (Customer, Employee, Chef, Server, Manager).
- **foods/**: Contains classes for different food items such as Burger, Pizza, and Drinks.
- **order/**: Contains classes related to orders placed by customers.
- **menu/**: Contains classes for managing the restaurant's menu.
- **restaurant/**: Contains classes for managing the restaurant, including finances and employees.
- **main.py**: The main script that integrates all modules and runs the restaurant management system.

## Features

1. **Users Management**:

   - Different types of users (Customer, Chef, Server, Manager) with specific functionalities.
   - Customers can place orders, pay bills, give tips to servers, and write reviews.
   - Employees receive salaries and manage orders.

2. **Food Menu**:

   - Supports various food items such as Pizzas, Burgers, and Drinks.
   - Menu management includes adding, removing, and displaying menu items.

3. **Order Management**:

   - Customers can place orders consisting of multiple food items.
   - Orders are added to the restaurant's order list for further processing.

4. **Financial Management**:

   - Tracks restaurant revenue, expenses, balance, and profits.
   - Supports payment processing for customer orders.

5. **Employee Management**:
   - Adds employees to the restaurant (Chef, Server, Manager).
   - Tracks employee salaries and manages payments.

## Usage

1. Clone the repository:

```
git clone https://github.com/Nirob844/restaurent_management
   cd restaurent_management
```

2. Run the main script:
   python main.py


## Dependencies

- Python 3.x
- No additional dependencies required.

## Contributing

Contributions are welcome! Please feel free to fork the repository and submit pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
