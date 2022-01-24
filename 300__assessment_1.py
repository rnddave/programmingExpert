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
        # Write your code here.
        pass

    def add_item(self, name, price, quantity):
        # Write your code here.
        pass

    def delete_item(self, name):
        # Write your code here.
        pass

    def get_items_in_price_range(self, min_price, max_price):
        # Write your code here.
        pass

    def get_most_stocked_item(self):
        # Write your code here.
        pass