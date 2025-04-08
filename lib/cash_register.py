#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.total = 0
    self.discount = discount
    self.items=[]
  
  def add_item(self, title, price, quantity=1):
    self.total += price * quantity
    for i in range(quantity):
      self.items.append(title)
  
  def apply_discount(self):
    if self.discount >0:
      discount_price = self.total * self.discount /100
      self.total -= discount_price
      print(f"After the discount, the total comes to ${int(self.total)}.")
    else:
      print("There is no discount to apply.")

new_register = CashRegister(10)

new_register.add_item("eggs", 0.98)
new_register.add_item("book", 5.00, 3)
new_register.apply_discount()
print(f"{new_register.total}")
print(f"{new_register.items}")