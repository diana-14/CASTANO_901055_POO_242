class ProductInventory:
    def _init_(self, product):
        self.product = product
        self.__stock = 0

    def add_stock(self, quantity):
        self.__stock += quantity

    def remove_stock(self, quantity):
        if quantity <= self.__stock:
            self.__stock-= quantity

    def show_stock(self):
        return f"Para el producto {self.product} hay un stock de {self.__stock}"

inventory = ProductInventory("Coca-Cola")
inventory.add_stock(100)
inventory.remove_stock(20)

#inventor.__stock = 100

print(inventory.show_stock())