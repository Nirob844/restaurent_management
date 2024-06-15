from users.users import User


class Customer(User):
    def __init__(self, name, phone, email, address, money) -> None:
        super().__init__(name, phone, email, address)
        self.wallet = money
        self._order = None
        self.due_amount = 0

    @property
    def order(self):
        return self._order
    
    @order.setter
    def order(self, order):
        self._order = order

    def place_order(self, order):
        self.order = order
        self.due_amount += order.bill
        print(f'{self.name} placed an order with bill ${order.bill:.2f}')

    def eat_food(self):
        print(f'{self.name} is eating food.')

    def pay_for_order(self, amount, restaurant):
        if amount >= self.due_amount:
            change = restaurant.receive_payment(self.order, amount, self)
            self.wallet -= amount
            print(f'{self.name} paid ${amount:.2f}. Change: ${change:.2f}')
        else:
            print('Not enough money to pay the bill.')

    def give_tips(self, server, tips_amount):
        if self.wallet >= tips_amount:
            self.wallet -= tips_amount
            server.receive_tips(tips_amount)
            print(f'{self.name} gave ${tips_amount:.2f} tips to {server.name}')
        else:
            print('Not enough money to give tips.')

    def write_review(self, stars):
        print(f'{self.name} gave {stars} stars.')

    def get_details(self):
        return f'Customer: {self.name}, Wallet: ${self.wallet:.2f}'