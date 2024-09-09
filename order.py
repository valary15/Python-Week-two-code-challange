# order.py
from customer import Customer  # Import the Customer class
from coffee import Coffee      # Import the Coffee class

class Order:
    all_orders = []  # Class variable to store all Order instances

    def __init__(self, customer, coffee, price):
        if not isinstance(customer, Customer):
            raise TypeError("Customer must be of type Customer.")
        if not isinstance(coffee, Coffee):
            raise TypeError("Coffee must be of type Coffee.")
        if not isinstance(price, (float, int)) or not (1.0 <= price <= 10.0):
            raise ValueError("Price must be a float between 1.0 and 10.0.")

        self._customer = customer
        self._coffee = coffee
        self._price = float(price)

        Order.all_orders.append(self)

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self):
        return self._price


if __name__ == "__main__":
    # Basic test cases
    from customer import Customer
    from coffee import Coffee

    customer = Customer("Bob")
    coffee = Coffee("Mocha")
    order = Order(customer, coffee, 5.5)

    print(order.customer.name)  # Bob
    print(order.coffee.name)  # Mocha
    print(order.price)  # 5.5
