class BankAccount:
  def __init__(self, account_number, account_holder_name, initial_balance):
      self.__account_number = account_number
      self.__account_holder_name = account_holder_name
      self.__account_balance = initial_balance

  def deposit(self, amount):
      if amount > 0:
          self.__account_balance += amount
          print(f"Deposited ₹{amount}. New balance: ₹{self.__account_balance}")
      else:
          print("Invalid deposit amount. Amount must be greater than 0.")

  def withdraw(self, amount):
      if 0 < amount <= self.__account_balance:
          self.__account_balance -= amount
          print(f"Withdrew ₹{amount}. New balance: ₹{self.__account_balance}")
      else:
          print("Invalid withdrawal amount or insufficient funds.")

  def display_balance(self):
      print(f"Account Balance for {self.__account_holder_name} (Account #{self.__account_number}): ₹{self.__account_balance}")


my_account = BankAccount("12345", "SANTHOSH", 1000)
print("Welcome to My Bank")

while True:
  print("1. Check balance\n2. Deposit\n3. Withdraw\n4. Exit")
  choice = int(input("Enter Your Choice: "))

  if choice == 1:
      my_account.display_balance()
  elif choice == 2:
      n = int(input("Enter the amount to deposit: "))
      my_account.deposit(n)
      print("Amount Deposited Successfully")
  elif choice == 3:
      m = int(input("Enter the amount to withdraw: "))
      my_account.withdraw(m)
  elif choice == 4:
      print("Thank you for using My Bank. Goodbye!")
      break
  else:
      print("Invalid choice. Please select a valid option.")