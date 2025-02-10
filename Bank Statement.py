data = [
  (749.17, "Investment Return"),
  (-11.54, "Utilities"),
  (-247.58, "Online Shopping"),
  (981.17, "Investment Return"),
  (-410.65, "Rent"),
  (310.60, "Rent"),
  (563.70, "Gift"),
  (220.79, "Salary"),
  (-49.85, "Car Maintenance"),
  (308.49, "Salary"),
  (-205.55, "Car Maintenance"),
  (870.64, "Salary"),
  (-881.51, "Utilities"),
  (518.14, "Salary"),
  (-264.66, "Groceries")
]


def print_transactions(transactions):
  for transaction in transactions:
    amount, statement = transaction
    print(f"{amount} - {statement}")


def print_summary(transactions):
  deposits = [transaction[0] for transaction
  in transactions if transaction[0] >= 0]

  total_deposited = sum(deposits)
  print(total_deposited)


  withdrawals = [transaction[0] for transaction
  in transactions if transaction[0] < 0]

  total_withdrawn = sum(withdrawals)
  print(total_withdrawn)

  balance = total_deposited + total_withdrawn
  print(balance)


def analyze_transactions (transactions):
  (transactions).sort()
  largest_withdrawal = transactions[0]
  largest_deposit = transactions[-1]
  print (f"Largest Withdrawal: {largest_withdrawal}")
  print (f"Largest Deposit: {largest_deposit}")

  deposits = [transaction[0] for transaction
  in transactions if transaction[0] >= 0]

  total_deposited = sum(deposits)
  average_deposit = total_deposited / len(deposits) if deposits else 0
  print(f"Average Deposit: {average_deposit}")

  withdrawals = [transaction[0] for transaction
  in transactions if transaction[0] < 0]

  total_withdrawals = sum(withdrawals)
  average_withdrawal = total_withdrawals / len(withdrawals) if withdrawals else 0
  print(f"Average Withdrawal: {average_withdrawal}")


print ("\nTransaction Analyzer")
print ("1. Print Transactions")
print ("2. Analyze Transactions")
print ("3. Stop Analyzer")
while True:
  choice = input("would you like to print, analyze, or stop? ")
  if choice == "print" or 1:
    print_summary(data)
  if choice == "analyze" or 2:
    analyze_transactions(data)
  if choice == "stop" or 3:
    break
  else:
    print("Invalid choice")
