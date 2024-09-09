# main.py
from customer import Customer
from coffee import Coffee
from order import Order

# Test cases
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
