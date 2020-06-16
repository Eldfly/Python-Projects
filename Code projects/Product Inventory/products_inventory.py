# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 08:45:12 2020

@author: Sofia
"""
class Product():
    
    product_id = 0
    
    def __init__ (self, name, price, quantity):
        
        Product.product_id += 1
        
        self.name = name
        self.price = price
        self.quantity = quantity
        self.product_id = Product.product_id
        

class Inventory():
    
        inventory_id = 0
        total_quanity = 0
        all_products = ''
    
        def __init__ (self, products=None):
            
            self.inventory_id += 1
            
            if products is None:
                self.products = []
            else:
                self.products = products
    
        def add_products(self, product):
            
            if product not in self.products:
                self.products.append(product)
                
        def remove_product(self, product):
            
            if product in self.products:
                self.products.remove(product)
                return f'{product.name} is removed from the  inventory'
            else:
                return 'Product not in stock'
                
        def various_products(self):
            
            print('Id Name Price Quantity')
            for prods in self.products:
                 #self.all_products += str(prods.product_id) + prods.name + str(prods.price) + str(prods.quantity) + '\n'
                print(str(prods.product_id) + ' ' + prods.name + ' ' + str(prods.price) + ' ' + str(prods.quantity))
         
        def total_amount(self):
            
            self.total_quanity = 0
            
            for prods in self.products:
                
                self.total_quanity +=  prods.quantity
                
            return f'The total amount of products in the inventory is {self.total_quanity}'
