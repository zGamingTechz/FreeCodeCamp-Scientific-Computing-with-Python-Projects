#took help from Landon Schlangen on yt
class Category:

  #this one runs by default
  def __init__(self, name):
    self.name = name
    self.ledger = []

  #this will diposit
  def deposit(self, amount, description=""):
    self.ledger.append({"amount": amount, "description": description})

  #this will withdraw
  def withdraw(self, amount, description=""):
    if self.check_funds(amount):
      self.ledger.append({"amount": -amount, "description": description})
      return True
    return False

  #this will fetch balanse
  def get_balance(self):
    totalCash = 0
    for item in self.ledger:
      totalCash += item["amount"]
    return totalCash

  #this will transwfer money
  def transfer(self, amount, category):
    if self.check_funds(amount):
      self.withdraw(amount, "Transfer to " + category.name)
      category.deposit(amount, "Transfer from " + self.name)
      return True
    return False

  #this will check funds
  def check_funds(self, amount):
    if self.get_balance() >= amount:
      return True
    return False

  #this will print object
  def __str__(self):
    title = f"{self.name:*^30}\n"
    items = ""
    total = 0
    for item in self.ledger:
      items += f"{item['description'][0:23]:23}" + f"{item['amount']:>7.2f}" + '\n'
      total += item['amount']
    output = title + items + "Total: " + str(total)
    return output

  #function for chart
  def get_withdrawls(self):
    total = 0
    for item in self.ledger:
      if item["amount"] < 0:
        total += item["amount"]
    return total


#hard thing
def create_spend_chart(categories):

  totals = {}
  
  for category in categories:
      total = 0
      for item in category.ledger:
          if item["amount"] < 0:
              total -= item["amount"]
      totals[category.name] = total
  
  total = sum(totals.values())
  percentages = {}
  
  for category in categories:
    percentages[category.name] = int(totals[category.name] / total * 100)
  
  output = "Percentage spent by category\n"
  
  for i in range(100, -10, -10):
    output += str(i).rjust(3) + "| "
  
    for category in categories:
        if percentages[category.name] >= i:
            output += "o  "
        else:
            output += "   "
  
    output += "\n"
  
  output += "    " + "-" * (len(categories) * 3 + 1) + "\n"
  max_length = max(len(category.name) for category in categories)
  
  for i in range(max_length):
    output += "     "
  
    for category in categories:
      if i < len(category.name):
        output += category.name[i] + "  "
      else:
        output += "   "
  
    if i < max_length - 1:
      output += "\n"
  
  return output
