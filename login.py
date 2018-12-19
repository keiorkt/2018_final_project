import csv

class Login:
  def validate_password(self, attemps):
    print(f"{self.user_name} : please enter your password")
    print(f"{attemps} attemps left")
    password = input()
    if password ==  self.accounts[self.user_id]['pw']:
      print("Logged in")
    elif attemps == 0:
      print("Your account is locked please contact the support center")
      raise 'Account authentication failed'
    else:
      self.validate_password(attemps-1)

  def ask_user_name(self, attemps):
    if attemps == 0:
      print("Your account is locked please contact the support center")
      raise 'Account authentication failed'
    print(f"{attemps} attemps left")
    self.read_account_csv()
    print("Hello, plase enter your user ID")
    self.user_id = input()
    if self.user_id not in self.accounts.keys():
      self.ask_user_name(attemps-1)
    print("Hello, plase enter your user name")
    self.user_name = input()
    if self.user_name != self.accounts[self.user_id]['user_name']:
      self.ask_user_name(attemps-1)
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
      print(self.accounts)

obj = Login()
obj.ask_user_name(5)

