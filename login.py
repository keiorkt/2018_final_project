import csv

# このクラスを使用すればログインをすることができる
class Login:
  def validate_password(self, attempts):
    print(f"{attempts} attempts left : {self.user_name} please enter your password")
    password = input()
    if password ==  self.accounts[self.user_id]['pw']:
      print("Logged in!!!")
    elif attempts == 0:
      print("Your account is locked please contact the support center")
      raise 'Account authentication failed'
    else:
      self.validate_password(attempts-1)

  def ask_user_name(self, attempts):
    if attempts == 0:
      print("Your account is locked please contact the support center")
      raise 'Account authentication failed'
    print(f"{attemps} attemps left")
    self.read_account_csv()
<<<<<<< HEAD
    print("Hello, plase enter your user ID")
    self.user_id = input()
    if self.user_id not in self.accounts.keys():
      self.ask_user_name(attemps-1)
    print("Hello, plase enter your user name")
    self.user_name = input()
    if self.user_name != self.accounts[self.user_id]['user_name']:
      self.ask_user_name(attemps-1)
=======
    print(f"{attempts} attempts left : Hello, plase enter your user ID")
    self.user_id = input()
    if self.user_id not in self.accounts.keys():
      print("Invalid user_id please enter the correct one")
      self.ask_user_name(attempts-1)
    print(f"{attempts} attempts left : Hello, plase enter your user name")
    self.user_name = input()
    if self.user_name != self.accounts[self.user_id]['user_name']:
      print("Invalid user_name please enter the correct user_name")
      self.ask_user_name(attempts-1)
>>>>>>> 55e26a03af0d33a11dcfca3d14d233a77f77bba1
    self.validate_password(5)

  def read_account_csv(self):
    with open('account.csv') as input_file:
      accounts = {}
      reader = csv.reader(input_file)
      next(reader, None)
      for line in reader:
        account = {}
        
        account['user_name'] = line[1]
        account['pw'] = line[2]
        accounts[line[0]] = account
      self.accounts = accounts

obj = Login()
obj.ask_user_name(5)
