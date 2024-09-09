# main.py
from customer import Customer
from coffee import Coffee

# Create customers
customer1 = Customer("Alice")
customer2 = Customer("Bob")

# Create coffees
coffee1 = Coffee("Espresso")
coffee2 = Coffee("Latte")

# Create orders
customer1.create_order(coffee1, 5.0)
customer1.create_order(coffee2, 6.0)
customer2.create_order(coffee1, 4.5)
customer2.create_order(coffee2, 7.0)

# Check orders for customer1
print(f"{customer1.name} has ordered: {[order.coffee.name for order in customer1.orders()]}")

# Check unique coffees ordered by customer1
print(f"{customer1.name} has tried: {[coffee.name for coffee in customer1.coffees()]}")

# Check number of orders for a specific coffee
print(f"{coffee1.name} has been ordered {coffee1.num_orders()} times.")

# Check the average price of a coffee
print(f"The average price of {coffee1.name} is ${coffee1.average_price():.2f}.")
