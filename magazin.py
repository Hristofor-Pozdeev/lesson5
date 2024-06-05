class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]

    def get_price(self, item_name):
        return self.items.get(item_name)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price

# Создание объектов класса Store
store1 = Store("Магазин овощей", "ул. Ленина, 10")
store1.add_item("яблоки", 0.5)
store1.add_item("бананы", 0.75)

store2 = Store("Магазин мяса", "пр. Победы, 5")
store2.add_item("говядина", 5)
store2.add_item("курица", 3)

store3 = Store("Магазин канцтоваров", "ул. Пушкина, 15")
store3.add_item("ручка", 1)
store3.add_item("тетрадь", 2)

print(f"{store1.name} ({store1.address}): {store1.items}")
print(f"{store2.name} ({store2.address}): {store2.items}")
print(f"{store3.name} ({store3.address}): {store3.items}")