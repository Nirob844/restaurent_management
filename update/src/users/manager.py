from employee import Employee


class Manager(Employee):
    def __init__(self, name, phone, email, address, salary, starting_date, department) -> None:
        super().__init__(name, phone, email, address, salary, starting_date, department)

    def manage_restaurant(self):
        print(f'{self.name} is managing the restaurant.')