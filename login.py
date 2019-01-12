
teacher_accounts = {'id_1':'password_1', 'id_2':'password_2'}

def validate_password(attempts, accounts, user_id):
  print(f"hello {user_id}, please input your password. {attempts} attempts left")
  password = input()
  if attempts == 0:
    print("your account is locked")
    return False
  elif password == accounts[user_id]:
    print("logged in.")
    return True
  else:
    validate_password(attempts-1, accounts, user_id)

def ask_user_name(accounts):
  account_keys = list(accounts.keys())
  print(f"please input your user ID.")
  user_id = input()
  if user_id in account_keys:
    validate_password(5, accounts, user_id)
  else:
    print("invalid username try again")
    ask_user_name(accounts)

ask_user_name(teacher_accounts)