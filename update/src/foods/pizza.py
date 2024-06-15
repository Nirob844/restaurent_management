from foods.foods import Food


class Pizza(Food):
    def __init__(self, name, price, size, toppings) -> None:
        super().__init__(name, price)
        self.size = size
        self.toppings = toppings

    def prepare(self):
        print(f'Preparing Pizza: {self.name} of size {self.size} with toppings {", ".join(self.toppings)}')