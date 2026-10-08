
class Atm:
  def __init__(self):
    self.balance = 0
    self.pin = 0
    self.display()

  def display(self):
    user_input = input("""
    1.Setpin
    2.Deposit
    3.Withdwar
    4.check_balance
    5.Exit
    """)
    if user_input == "1":
      self.create_pin()
    elif user_input =="2":
      self.deposit()
    elif user_input =="3":
      self.withdwar()
    elif user_input =="4":
      self.check_balance()
    else:
      print("Exit")


  def create_pin(self):
    self.pin = input("Enter your pin for create")
    print("Pin successfully created!")
    self.display()



  def deposit(self):
    new_pin = input("Enter your pin ")
    if new_pin == self.pin:
      amount = float(input("Enter amount to deposit"))
      self.balance += amount
      print("deposit")
    else:
      print("Wrong pin ")
    self.display()




  def withdwar(self):
    new_pin = input("Enter your pin ")
    if new_pin == self.pin:
      new_amount = float(input("Enter amount to withdraw"))
      if self.balance > new_amount:
        self.balance -= new_amount
        print("Withdraw Successfully!")
      else:
        print("Insufficent amount")
    else:
      print("Wrong pin ")
    self.display()





  def check_balance(self):
    new_pin = input("Enter your pin ")
    if new_pin == self.pin:
      print("Balance = ",self.balance)
    else:
       print("Wrong pin ")

    self.display()







