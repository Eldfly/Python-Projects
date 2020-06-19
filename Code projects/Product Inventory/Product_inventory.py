# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 11:25:15 2020

@author: Sofia


Create an application which manages an inventory of products. Create a product class which has a price, id, and quantity on hand. 
Then create an inventory class which keeps track of various products and can sum up the inventory value.

"""

            

#create some products
milk = Product('Milk', 12.50, 20)
butter = Product('Butter', 25, 30)
cheese = Product('Cheese', 70, 10)
egg = Product('Egg 10/p', 40, 20)

#create a new inventory and add my products
inventory = Inventory([milk,butter,cheese,egg])

#print out all the products in my inventory
inventory.various_products()

#print out the total amount of products in the inventory
inventory.total_amount()



