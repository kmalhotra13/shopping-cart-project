# shopping_cart.py

import time

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

tax_rate = 0.06
sale = []

def to_usd(amount):
    two_decimal = "{0:.2f}".format(amount)
    dollar_str = f'${two_decimal}'
    return dollar_str

def tax(amount):
    tax_amount = amount * tax_rate
    return tax_amount

def total(amount):
    total_var = amount + tax(amount)
    return total_var

def lookup_product(x):
    result = ""
    for product in products:
        if product["id"] == x:
            result = ("Name: " + product["name"] + " | Price: " + to_usd(product["price"]))
    return result

def line():
    print("-" * 50)

def scan(item):
    x=int(item)
    for product in products:
        if product["id"] == x:
            sale.append({"name": product["name"], "price": product["price"]})

def subtotal():
    subtotal = 0
    for product in sale:
         subtotal = subtotal + float(product["price"])
    return subtotal

def get_time():
    pretty_time = time.strftime('%X %x %Z').center(50, " ")
    return pretty_time


if __name__ == '__main__':

    while True:
        x = input("Please input a product id (type 'exit' to exit or 'lookup' to look up a product):")
        if x == "exit":
            break
        elif x == "lookup":
            pid = input("Please input a product id to lookup: ")
            response = lookup_product(int(pid))
            print(response)
        else: scan(x)
        

    # Final Receipt Output:

    line()

    # Header:
    line()
    print("".center(50," "))
    print("Tesco Metro".center(50, " "))
    print("Magdalen St, Oxford OX1 3AD, UK".center(50, " "))
    print("www.tesco.com".center(50, " "))
    print("+44 0345 026 9682".center(50, " "))
    print(get_time())
    print("".center(50," "))
    line()
    print("")
    # End Header

    # Print items:

    print("Shopping List:")
    for product in sale:
         price_usd = to_usd(product["price"])
         print(" • " + product["name"] + f" ({price_usd})")
    print("")
    line()
    print("")

    # Print totals:
    subtotal = subtotal()
    subtotal_string = to_usd(subtotal)
    sales_tax = to_usd(tax(subtotal))
    total_string = to_usd(total(subtotal))

    print(f"Subtotal: {subtotal_string}")
    print(f"Sales Tax (6.00%): {sales_tax}")
    print(f"Total: {total_string}")
    print("")
    line()
    print("")

    # Print Footer:


    print("Thank you for shopping at Tesco Metro!".center(50, " "))
    print("Have a great day!".center(50, " "))
    line()