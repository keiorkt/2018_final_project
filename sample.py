import csv
with open('account.csv') as input_file:
  accounts = {}
  reader = csv.reader(input_file)
  next(reader, None)
  for line in reader:
    account = {}
    account['user_name'] = line[1]
    account['pw'] = line[2]
    accounts[line[0]] = account
  print(accounts)
