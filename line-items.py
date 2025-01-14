from os import listdir
from os.path import isfile, join, exists
import json
from pprint import pprint
from dateutil.parser import parse

transaction_files_dir = "./transactions"
if not exists(transaction_files_dir):
  print("ERROR: You need to download the transactions and put them in ./transactions")
  exit(1)

transaction_files = [f"{transaction_files_dir}/{f}" for f in listdir(transaction_files_dir) if isfile(join(transaction_files_dir, f))]
transactions = []

for name in transaction_files:
  print(name)
  with open(name) as f:
    transactions += json.load(f)["transactions"]

transactions = sorted(transactions, key=lambda t: parse(t["transactionDetail"]["transactionDate"]))

def pad(s):
  if len(s) < 6:
    return s + (" " * (6 - len(s)))
  return s

total_per_year = {}

print("Transactions")
print("------------------------------")
for t in transactions:
  date = parse(t["transactionDetail"]["transactionDate"])
  line_items = t.get("additionalInfo", {}).get("orderItems", [])
  for item in line_items:
    val = item["totalPrice"]["value"]
    total_per_year[date.year] = total_per_year.get(date.year, 0) + val
    if val > 0:
      print(f"{date.strftime('%d-%m-%Y')}\t{pad(item['totalPrice']['formattedValue'])}\t{item['productName']}")

print("------------------------------")
print("Subtotal by year")
print("------------------------------")
total = 0
for year, amount in total_per_year.items():
  total += amount
  print(f"{year}: £{amount / 100}")

print("=============================")
print(f"Total spend: £{total / 100}")
print("=============================")