class Order:
    def __init__(self, customer, items) -> None:
        self.customer = customer
        self.items = items
        self.bill = sum(item.price for item in items)

    def __str__(self):
        item_details = ', '.join([item.name for item in self.items])
        return f"Order by {self.customer.name}: {item_details} | Total Bill: ${self.bill:.2f}"