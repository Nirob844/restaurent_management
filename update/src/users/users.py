from abc import ABC, abstractmethod


# Abstract User Class
class User(ABC):
    def __init__(self, name, phone, email, address) -> None:
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    @abstractmethod
    def get_details(self):
        pass