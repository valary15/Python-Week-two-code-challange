# coffee.py
from order import Order


class Coffee:
    def __init__(self, name):
        self._name = name  # Name cannot be changed after initialization

    @property
    def name(self):
        return self._name

    # Return all orders for this coffee
    def orders(self):
        return [order for order in Order.all_orders if order.coffee == self]

    # Return a unique list of customers who ordered this coffee
    def customers(self):
        return list(set(order.customer for order in self.orders()))

    # Return the total number of orders for this coffee
    def num_orders(self):
        return len(self.orders())

    # Return the average price of all orders for this coffee
    def average_price(self):
        if self.num_orders() == 0:
            return 0
        total_price = sum(order.price for order in self.orders())
        return total_price / self.num_orders()


if __name__ == "__main__":
    # Basic test cases
    from customer import Customer

    customer1 = Customer("Alice")
    coffee1 = Coffee("Cappuccino")
    coffee2 = Coffee("Latte")

    customer1.create_order(coffee1, 5.0)
    customer1.create_order(coffee2, 6.5)

    print(coffee1.name)  # Cappuccino
    print(coffee1.orders())  # [Order instance]
    print(coffee1.customers())  # [Customer instance for Alice]
    print(coffee1.num_orders())  # 1
    print(coffee1.average_price())  # 5.0
