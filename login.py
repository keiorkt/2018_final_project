
def validate_password(attempts, accounts, user_id):
  password = input(f"hello {user_id}, please input your password. {attempts} attempts left : ")
  if attempts == 0:
    print("your account is locked")
    return False
  elif password == accounts[user_id]:
    print("logged In")
    return True
  else:
    validate_password(attempts-1, accounts, user_id)

def ask_user_name(accounts):
  account_keys = list(accounts.keys())
  user_id = input("please input your user ID : ")
  if user_id in account_keys:
    return validate_password(5, accounts, user_id)
  else:
    print("invalid username try again")
    ask_user_name(accounts)
