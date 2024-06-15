from users.users import User


class Employee(User):
    def __init__(self, name, phone, email, address, salary, starting_date, department) -> None:
        super().__init__(name, phone, email, address)
        self.salary = salary
        self.due = salary
        self.starting_date = starting_date
        self.department = department

    def receive_salary(self):
        self.due = 0
        print(f'{self.name} received salary.')

    def get_details(self):
        return f'Employee: {self.name}, Department: {self.department}, Salary: ${self.salary:.2f}'
