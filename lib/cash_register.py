#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.total = 0
    self.discount = discount
    self.items=[]
    self.last_transaction = []
  
  def add_item(self, title, price, quantity=1):
    self.total += price * quantity
    for i in range(quantity):
      self.items.append(title)
      self.last_transaction=[price, quantity]
  
  def apply_discount(self):
    if self.discount >0:
      discount_price = self.total * self.discount /100
      self.total -= discount_price
      print(f"After the discount, the total comes to ${int(self.total)}.")
    else:
      print("There is no discount to apply.")

  def void_last_transaction(self):
    if self.last_transaction:
      price, quantity = self.last_transaction
      self.total -= price * quantity
      for i in range(quantity):
        if self.items:
          self.items.pop()
        else:
          print("No transactions to void")


new_register = CashRegister(10)

new_register.add_item("eggs", 0.98)
new_register.add_item("book", 5.00, 3)
new_register.add_item("macbook", 800.00, 2)
new_register.apply_discount()

print(f"{new_register.total}")
print(f"{new_register.items}")
new_register.void_last_transaction()
print(f"{new_register.items}")