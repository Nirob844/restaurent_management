from foods import Food


class Drinks(Food):
    def __init__(self, name, price, is_cold=True) -> None:
        super().__init__(name, price)
        self.is_cold = is_cold

    def prepare(self):
        print(f'Preparing Drink: {self.name}, {"Cold" if self.is_cold else "Hot"}')