from foods import Food


class Burger(Food):
    def __init__(self, name, price, meat, ingredients) -> None:
        super().__init__(name, price)
        self.meat = meat
        self.ingredients = ingredients

    def prepare(self):
        print(f'Preparing Burger: {self.name} with {self.meat} and {", ".join(self.ingredients)}')