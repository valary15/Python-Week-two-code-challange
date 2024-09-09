# customer.py

class Customer:
    all_customers = []  # Class variable to store all Customer instances

    def __init__(self, name):
        self.name = name  # This invokes the name setter
        Customer.all_customers.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise ValueError("Name must be a string between 1 and 15 characters.")

    # Return all orders for this customer
    def orders(self):
        from order import Order  # Local import
        return [order for order in Order.all_orders if order.customer == self]

    # Return all coffees for this customer
    def coffees(self):
        return list(set(order.coffee for order in self.orders()))

    # Create a new order
    def create_order(self, coffee, price):
        from order import Order  # Local import
        return Order(self, coffee, price)
