# customer.py
from order import Order


class Customer:
    all_customers = []  # Class variable to store all Customer instances

    def __init__(self, name):
        self.name = name  # Will invoke the name setter
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
        return [order for order in Order.all_orders if order.customer == self]

    # Return a unique list of all coffees ordered by this customer
    def coffees(self):
        return list(set(order.coffee for order in self.orders()))

    # Create a new order for this customer
    def create_order(self, coffee, price):
        return Order(self, coffee, price)


if __name__ == "__main__":
    # Basic test cases
    from coffee import Coffee

    customer1 = Customer("John")
    customer2 = Customer("Sara")
    coffee1 = Coffee("Espresso")
    coffee2 = Coffee("Latte")

    customer1.create_order(coffee1, 5.0)
    customer1.create_order(coffee2, 6.0)
    customer2.create_order(coffee1, 4.5)

    print(customer1.name)  # John
    print(customer1.orders())  # [Order instance for Espresso, Latte]
    print(customer1.coffees())  # [Coffee instances for Espresso, Latte]
