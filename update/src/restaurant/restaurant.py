from menu.menu import Menu


class Restaurant:
    def __init__(self, name, rent) -> None:
        self.name = name
        self.rent = rent
        self.orders = []
        self.employees = {'chef': None, 'server': None, 'manager': None}
        self.menu = Menu()
        self.revenue = 0
        self.expense = 0
        self.balance = 0

    def add_employee(self, employee_type, employee):
        if employee_type in self.employees:
            self.employees[employee_type] = employee

    def add_order(self, order):
        self.orders.append(order)

    def receive_payment(self, order, amount, customer):
        if amount >= order.bill:
            self.revenue += order.bill
            self.balance += order.bill
            customer.due_amount = 0
            return amount - order.bill
        else:
            print('Not enough money. Pay more.')
            return 0

    def pay_expense(self, amount, description):
        if amount <= self.balance:
            self.expense += amount
            self.balance -= amount
            print(f'Expense ${amount:.2f} for {description}')
        else:
            print(f'Not enough money to pay ${amount:.2f}.')

    def pay_salary(self, employee):
        print(f'Paying salary for {employee.name}, Salary: ${employee.salary:.2f}')
        if employee.salary <= self.balance:
            self.balance -= employee.salary
            self.expense += employee.salary
            employee.receive_salary()
        else:
            print(f'Not enough balance to pay {employee.name}.')

    def show_employees(self):
        print(f'-----------SHOWING EMPLOYEES--------')
        for role, employee in self.employees.items():
            if employee is not None:
                print(f'{role.capitalize()}: {employee.name}, Salary: ${employee.salary:.2f}')

    def show_menu(self):
        return self.menu.show_menu()

    def show_orders(self):
        return '\n'.join([str(order) for order in self.orders])