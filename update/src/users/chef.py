from employee import Employee


class Chef(Employee):
    def __init__(self, name, phone, email, address, salary, starting_date, department, specialty) -> None:
        super().__init__(name, phone, email, address, salary, starting_date, department)
        self.specialty = specialty

    def cook_food(self, order):
        print(f'{self.name} is cooking {", ".join([item.name for item in order.items])}.')