from employee import Employee


class Server(Employee):
    def __init__(self, name, phone, email, address, salary, starting_date, department) -> None:
        super().__init__(name, phone, email, address, salary, starting_date, department)
        self.tips_earning = 0
    
    def take_order(self, order):
        print(f'{self.name} took an order from {order.customer.name}.')

    def transfer_order(self, order, chef):
        print(f'{self.name} transferred order for {order.customer.name} to the chef {chef.name}.')

    def serve_food(self, order):
        print(f'{self.name} served food to {order.customer.name}.')

    def receive_tips(self, amount):
        self.tips_earning += amount
        print(f'{self.name} received ${amount:.2f} in tips.')