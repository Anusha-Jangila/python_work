import sys
import requests
import json

if(len(sys.argv) < 2):
  sys.exit("Missing command-line argument")

try:
  n = float(sys.argv[1])
except ValueError:
  sys.exit("Command-line argument is not a number")

amount = 0
try:
  response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
  o = response.json()
  currencies = o["bpi"]
  usd = currencies["USD"]
  rate = usd["rate_float"]
  amount = n * rate
except requests.RequestException:
  sys.exit("Request to ConDesk has failed")

print(f"${amount:,.4f}")
