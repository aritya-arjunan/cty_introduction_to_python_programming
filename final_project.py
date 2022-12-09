# Define class Pizza
class Pizza:
    # Define Pizza attributes
    size = 'Small'
    toppings = 'Cheese'
    base = 'Thin & Crispy'
    crust = 'Stuffed'
    sauce = 'BBQ'
    quantity = 1
    price = 0
    
    # Initialise price maps of Pizza
    def __init__(self):
        self.size_price = {"Large" : 9, "Medium" : 6, "Small" : 3.5}
        self.toppings_price = {"Cheese" : 5, "Cheese & Mushrooms" : 10,
                "Cheese, Mushrooms & Pepperoni" : 20}
        self.base_price = {"Thin & Crispy" : 20.5, "Traditional" : 30}
        self.crust_price = {"Stuffed" : 7, "Hollow" : 4}
        self.sauce_price = {"Alfredo" : 1, "BBQ" : 7, "Tomato" : 10}
        
    # Setters and getters of Pizza attributes
    def set_size(self, size):
        self.size = size
    
    def get_size(self):
        return self.size

    def set_toppings(self, toppings):
        self.toppings = toppings

    def get_toppings(self):
        return self.toppings

    def set_base(self, base):
        self.base = base

    def get_base(self):
        return self.base
    
    def set_crust(self, crust):
        self.crust = crust

    def get_crust(self):
        return self.crust

    def set_sauce(self, sauce):
        self.sauce = sauce

    def get_sauce(self):
        return self.sauce

    def set_quantity(self, quantity):
        self.quantity = quantity

    def get_quantity(self):
        return self.quantity

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price
    
    def get_size_price(self):
        return self.size_price

    def get_toppings_price(self):
        return self.toppings_price

    def get_base_price(self):
        return self.base_price

    def get_crust_price(self):
        return self.crust_price

    def get_sauce_price(self):
        return self.sauce_price
        
    # Define behaviour method calculate_price
    def calculate_price(self):
        # Define a variable unit_price which is calculated by adding price 
        # of pizza attributes
        unit_price = self.size_price[self.size]
        unit_price += self.toppings_price[self.toppings]
        unit_price += self.base_price[self.base]
        unit_price += self.crust_price[self.crust]
        unit_price += self.sauce_price[self.sauce]
        # Define a variable called price that is calculated by multiplying 
        # unit_price by the pizza quantity
        price = unit_price * self.quantity
        # Set the pizza price
        self.set_price(price)

    # Define behaviour method save_order_ticket
    def save_order_ticket(self):
        filename = "order_ticket.txt"
        # Create a file if it does not exist or if it does exist, do nothing
        handle = open(filename, "a+")
        # Close the file
        handle.close()
        # Open the same file and overwrite it
        mynewhandle = open(filename, "w")
        # Write pizza order details
        mynewhandle.write("Here are your pizza order details:\n")
        mynewhandle.write("Size: %s\n" %self.size)
        mynewhandle.write("Toppings: %s\n" %self.toppings)
        mynewhandle.write("Base: %s\n" %self.base)
        mynewhandle.write("Crust: %s\n" %self.crust)
        mynewhandle.write("Sauce: %s\n" %self.sauce)
        mynewhandle.write("Quantity: %s\n" %self.quantity)
        mynewhandle.write("Price: $%s\n" %self.price)
        # Close the file
        mynewhandle.close()


# Define a function called get_selection that gets the selected pizza price
# map key
def get_selection(price_map):
    # ks is a list of price map keys
    ks = list(price_map.keys())
    # Print list of options from price_maps
    for x in range(len(ks)):
        print("Type %s to select %s ($%s)" %(str(x + 1), ks[x], 
            price_map[ks[x]]))
    # Get input from user to select which option they want
    selection = int(input("Your choice:"))
    # If the input from user is more than the length of ks, the input is not
    # valid, print warning message and go through this function again
    if selection > len(ks):
        print("Please enter a valid number\n")
        selected_key = get_selection(price_map)
    else:
        selected_key = ks[selection - 1]
    # Return selected key
    return selected_key 
    
# Define a function called display_menu
def display_menu(pizza):
    # Print menu with current pizza options and price
    print()
    print("Welcome to Aritya's Exquisite Pizza Restaurant!")
    print("Here are your options:")
    print("Type 1 to update your pizza size (current size: %s)" 
          %pizza.get_size())
    print("Type 2 to update your pizza toppings (current toppings: %s)" 
          %pizza.get_toppings())
    print("Type 3 to update your pizza base (current base: %s)" 
          %pizza.get_base())
    print("Type 4 to update your pizza crust (current crust: %s)" 
          %pizza.get_crust())
    print("Type 5 to update your pizza sauce (current sauce: %s)" 
          %pizza.get_sauce())
    print("Type 6 to update your pizza quantity (current quantity: %s)" 
          %pizza.get_quantity())
    print("Type 7 to save your order ticket")
    print("Type 8 to exit")
    # Calculate and print current pizza price
    pizza.calculate_price()
    print("The current price is $%s" %pizza.get_price())
    print()
    
    # Get user selection to build pizza 
    number_input = input("Your choice:")
    
    # Build pizza according to the selection
    if number_input == "1":
        selected_key = get_selection(pizza.get_size_price())
        pizza.set_size(selected_key)

    elif number_input == "2":
        selected_key = get_selection(pizza.get_toppings_price())
        pizza.set_toppings(selected_key)

    elif number_input == "3":
        selected_key = get_selection(pizza.get_base_price())
        pizza.set_base(selected_key)

    elif number_input == "4":
        selected_key = get_selection(pizza.get_crust_price())
        pizza.set_crust(selected_key)

    elif number_input == "5":
        selected_key = get_selection(pizza.get_sauce_price())
        pizza.set_sauce(selected_key)

    elif number_input == "6":
        quantity = int(input("How many pizzas do you want?"))
        pizza.set_quantity(quantity)

    # Calculate price and save order ticket
    elif number_input == "7":
        pizza.calculate_price()
        pizza.save_order_ticket()
        print("Your order ticket has been saved.")

    # Exit function if user wants to quit
    elif number_input == "8":
        return
    
    # If user didn't enter a valid option, print warning message
    else:
        print("Please enter a valid option")
    
    # Recurse
    display_menu(pizza)

# Create an object of class Pizza called p
p = Pizza()
# Call display_menu with the argument p
display_menu(p)
