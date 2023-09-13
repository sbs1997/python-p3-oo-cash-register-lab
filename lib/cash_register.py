class CashRegister:
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.last_transaction = {
      "title": "",
      "price": 0,
      "quantity": 0
    }

  def add_item(self, title, price, quantity=1):
    for index in range(quantity): 
      self.items.append(title)
    self.total += price*quantity
    self.last_transaction["title"] = title
    self.last_transaction["price"] = price
    self.last_transaction["quantity"] = quantity


  def apply_discount(self):
    if self.discount:
      self.total = self.total*(1 - self.discount*0.01)
      print(f"After the discount, the total comes to ${int(self.total)}.")
    else:
      print("There is no discount to apply.")

  def void_last_transaction(self):
    for index in range(self.last_transaction["quantity"]): 
      self.items.append(self.last_transaction["title"])
    self.total -= self.last_transaction["price"]*self.last_transaction["quantity"]