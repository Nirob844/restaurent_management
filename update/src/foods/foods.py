from abc import ABC, abstractmethod


class Food(ABC):
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price

    @abstractmethod
    def prepare(self):
        pass