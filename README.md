# Python-Week-two-code-challange

#cofee.py
-class Coffee:
The code def **init**(self, name), is used to initialise objects of a class and in this case coffee. a class is whereby the objects will be created, while the self.name in line 7 is used to hold the coffees name.

-the @properrty , line 10-12 : this code allows the access of an attribute in a given class, and in this case the access of the coffees name, which can be accessed but not changed.

-code line 14-15: These line of codes, ensures that order instances in relation to a specific coffee is returned through looping until the desired condition is met.The list comprehension iterates over each order in the Order.all_orders list. For each order, it checks if order.coffee matches the current Coffee instance (self).If the condition is True, the order is included in the resulting list. If the condition is False, that order is ignored. The method returns a list of orders where the coffee matches the current coffee.

-code line 18-19 : Method in the Coffee class that returns a unique list of customers who ordered a particular coffee. self.orders() gets all the orders for the current coffee. The code extracts the customer for each of those orders using order.customer.The set() ensures that each customer appears only once, even if they have placed multiple orders for the same coffee. The list() function converts the set of unique customers into a list.

-code line 22-23:The num_orders method calculates how many times a specific coffee (self) has been ordered by counting the number of entries in the list returned by the orders() method.

#Customer.py
Customer Class: Manages customer details, their orders, and can create new orders.
Instance Methods: orders() returns a list of orders for the customer; coffees() returns unique coffees ordered by the customer; create_order() creates a new order. Properties: name ensures the name adheres to validation rules and allows retrieval and updating of the customer's name.

Main.py
This code imports the Customer, Coffee, and Order classes from their respective modules.

Order.py
Class Variable: all_orders: A list that holds all instances of Order. This is used to keep track of every order created.

Initialization Method (**init**):Takes three parameters: customer, coffee, and price, and Validates, Customer, through Checking if the customer object has a name attribute (ensures it’s a Customer object). Coffee: Checks if the coffee object has a name attribute (ensures it’s a Coffee object) Price: Ensures that price is a number (float or int) within the range 1.0 to 10.0 and Initializes instance variables \_customer,coffee, and price to store the respective values, then Appends the created order to the all_orders list.

Properties: customer: Returns the customer associated with this order coffee: Returns the coffee associated with this order and price: Returns the price of the order.
