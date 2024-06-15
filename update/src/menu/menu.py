class Menu:
    def __init__(self) -> None:
        self.items = {'pizza': [], 'burger': [], 'drinks': []}

    def add_menu_item(self, item_type, item):
        if item_type in self.items:
            self.items[item_type].append(item)

    def remove_menu_item(self, item_type, item):
        if item_type in self.items and item in self.items[item_type]:
            self.items[item_type].remove(item)

    def show_menu(self):
        menu_str = "Menu:\n"
        for item_type, items in self.items.items():
            for item in items:
                menu_str += f'{item_type.capitalize()}: {item.name}, Price: ${item.price:.2f}\n'
        return menu_str