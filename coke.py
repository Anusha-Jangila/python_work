amount_due = 50
paid_amount = 0
while amount_due > 0
  print("Amount Due: " + str(amount_due))
  paid_amount = int(input("Insert Coin: "))
  if(paid_amount == 25 or paid_amount == 10 or paid_amount == 5):
    amount_due -= paid_amount
print("Change Owed: " + str(amount_due).lstrip('-'))
