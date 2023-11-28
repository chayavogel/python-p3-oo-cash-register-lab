#!/usr/bin/env python3

class CashRegister:
    
    latest_transaction_amount = 0

    def __init__(self, discount = 0):
        self.discount = discount
        self.total = 0
        self.items = []

    def add_item(self, item, price, quantity = 1):
        
        CashRegister.latest_transaction_amount = price * quantity

        self.total += (price * quantity)
        i = 0 
        while i < quantity:
            self.items.append(item)
            i+=1
        return self.items

    def apply_discount(self):
        if self.discount:
            self.total = self.total - (self.total * (self.discount / 100))
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else: 
            print("There is no discount to apply.")

    def void_last_transaction(self):
        self.total -= CashRegister.latest_transaction_amount


with_discount = CashRegister(20)
without_discount = CashRegister()

with_discount.add_item("Macbook", 1000)
without_discount.add_item("Macbook", 1000)
with_discount.apply_discount()
without_discount.apply_discount()

