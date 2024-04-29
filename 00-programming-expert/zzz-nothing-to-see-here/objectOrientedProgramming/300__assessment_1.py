## INVENTORY CLASS
"""
write a class as defined to handle management of inventory 

all instances of this class should be initialised by passing an integer value named [max_capacity]
that indicates the maximum number of items that can be stored in the inventory
your class will need to store items that are represented by a [name], [price], quantity.

Following methods: 

[add_item(name, price, quantity)]
- add item to inventory and return [True] if successful
- if over capacity, then return [False] and do not add item to inventory
- additionally, if an item with [name] already exists, then return [False] and do not add to inventory 

[delete_item(name)]
- delete an item from inventory and return [True] if successful 
- if no item in inventory with the [name] then return [False]

[get_most_stocked_item()]
- return name of item that has highest quantity in inventory
- return [None] if there are no items in the inventory
- can assume there will always be one item that has largest quantity (except when inventory is empty)

[get_items_in_price_range(min_price, max_price)]
- return list of names of the items that have a price within specified range 
"""

class Inventory:
    def __init__(self, max_capacity):
        self.max_capacity = max_capacity
        self.items = {}
        self.item_count = 0

    def add_item(self, name, price, quantity):
        # self.name = name
        # self.price = price
        # self.quantity = quantity
        
        if name in self.items:
            return False

        if self.item_count + quantity > self.max_capacity:
            return False

        self.items[name] = {"name": name, "price": price, "quantity": quantity}
        self.item_count += quantity
        return True

    def delete_item(self, name):
        # self.name = name

        if name not in self.items:
            return False

        self.item_count -= self.items[name]["quantity"]
        del self.items[name]
        return True

    def get_items_in_price_range(self, min_price, max_price):
        # self.min_price = min_price
        # self.max_price = max_price

        item_names = []

        for item in self.items.values():
            name = item["name"]
            price = item["price"]

            if min_price <= price <= max_price:
                item_names.append(name)

        return item_names

    def get_most_stocked_item(self):
        most_stocked_item_name = None
        largest_quantity = 0

        for item in self.items.values():
            name = item["name"]
            quantity = item["quantity"]

            if quantity > largest_quantity:
                most_stocked_item_name = name
                largest_quantity = quantity

        return most_stocked_item_name