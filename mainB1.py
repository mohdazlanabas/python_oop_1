class Item:
    pay_rate = 0.8 # after 20% discount 
    def __init__(self, name:str, price: float, quantity=1):
        
        assert price >= 0, f"Price {price} is not greater than zero1"
        assert quantity >= 0, f"Quantity{quantity} is not greater than zero1"
        
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price  * Item.pay_rate

item1 = Item("Phone", 100, 5)
item2 = Item("Laptop", 1000, 3)

print(Item.pay_rate)
print(item1.pay_rate)
print(item2.pay_rate)
print(Item.__dict__)
print(item1.__dict__)
print(item2.__dict__)