import csv

class Item:
    pay_rate = 0.8 # after 20% discount 
    all = [] 
    def __init__(self, name:str, price: float, quantity=1):
        
        assert price >= 0, f"Price {price} is not greater than zero1"
        assert quantity >= 0, f"Quantity{quantity} is not greater than zero1"
        
        self.name = name
        self.price = price
        self.quantity = quantity
        
        # Action to execute
        Item.all.append(self)
    
    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price  * self.pay_rate
        
    @classmethod
    def instantiate_from_csv(cls):
        with open('item.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
            
        for item in items:
            Item( 
                 name = item.get('name'),
                 price=int(item.get('price')),
                 quantity=int(item.get('quantity')),
                 )
    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
        
    def __repr__(self):
        return f"Item('{self.name}', '{self.price}', '{self.quantity}', )"

class Phone(Item):
    all = []
    def __init__(self, name:str, price: float, quantity=0, broken_phones=0):
        
        assert price >= 0, f"Price {price} is not greater than zero!"
        assert quantity >= 0, f"Quantity{quantity} is not greater than zero!"
        assert quantity >= 0, f"Broken Phones{broken_phones} is not greater than zero!"
        
        self.name = name
        self.price = price
        self.quantity = quantity
        self.broken_phones = broken_phones
        
        # Action to execute
        Phone.all.append(self)

phone1 = Item("jscPhonev10", 500, 3)
phone1.broken_phones = 1
phone2 = Item("jscPhonev20", 700, 5)
phone2.broken_phones = 1


