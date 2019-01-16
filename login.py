
is_logged_in = False
ATTEMPTS = 5

def ask_user_name(accounts):
  account_id = list(accounts.keys())
  user_id = input("please input your user ID :")
  if user_id in account_id:
    validate_password(accounts, ATTEMPTS, user_id)
  else:
    print("Invalid user id")
    ask_user_name(accounts)

def validate_password(accounts, attempts, user_id):
  global is_logged_in

  password = input(f"please input your password {attempts} attempts left:")
  if attempts == 0:
    print("Your account is locked.")
  elif accounts[user_id] == password:
    print("logged In")
    is_logged_in = True
  else:
    print("Invalid password")
    validate_password(accounts, attempts - 1, user_id)
