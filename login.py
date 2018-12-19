import csv

class Login:
  def validate_password(self,attemps):
    print(f"{self.user_name} : please enter your password")
    password = input()
    # if self.account[self.user_name] == password:
    if "password" == password:
      print("Logged in")
    elif attemps == 0:
      print("Your account is locked please contact the support center")
    else:
      self.validate_password(attemps-1)

  def ask_user_name(self):
    print("Hello, plase enter your user_name")
    # validation here
    self.user_name = input()
    self.validate_password(5)


obj = Login()
obj.ask_user_name()

#usei modified the code
