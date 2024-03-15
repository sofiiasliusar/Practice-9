class Order():
    '''
    Клас описує замовлення
    self.date - дата замовлення
    self.number - номер замовлення
    '''
    def __init__(self, date, number):
        self.date = date
        self.number = number

    def __str__(self):
        return f"Order: {self.date} | {self.number}"
    
    def confirm(self):
        print(f"Order {self.number} confirmed")

    def close(self):
        print(f"Order {self.number} closed")
    
class SpecialOrder(Order):
    '''
    Клас, що описує спеціальне замовлення
    self.private_client - чи є клієнт V.I.P.
    '''
    def __init__(self, date, number, private_client):
        super().__init__(date, number)
        self.private_client = private_client

    def __str__(self):
        return f"SpecialOrder: {self.date} | {self.number} | {self.private_client}"

    def dispatch(self):
        print(f"SpecialOrder: {self.number} dispatched")

class NormalOrder(Order):
    '''
    Клас, що описує замовлення
    '''
    def dispatch(self):
        print(f"NormalOrder: {self.number} dispatched")
    
    def receive(self):
        print(f"NormalOrder: {self.number} received")

class Customer():
    '''
    Клас, що описує користуача 
    self.name - ім'я користувача
    self.adress - адреса користувача
    '''
    def __init__(self, name, adress):
        self.name = name
        self.adress = adress

    def __str__(self):
        return f"Customer: {self.name} | {self.adress}"
    
    def send_order(self, order):
        print(f"Customer {self.name} sends order {order}")
    
    def receive_order(self, order):
        print(f"Customer {self.name} receives order {order}")

customer = Customer("Peter Parker", "123 main street")
order = NormalOrder('08.03.2024', 12345) 
customer.send_order(order)
order.confirm()
order.close()
order.dispatch()

special_order = SpecialOrder('08.03.2024', 54321, True)
special_order.dispatch()
special_order.close()