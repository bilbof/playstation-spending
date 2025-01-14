# PlayStation store spending

Calculate how much you spent on Playstation per year and export transactions.

## Output example

```
python ./line-items.py
15-04-2024 £2.99  Firewatch
12-05-2024 £19.99 ANIMAL WELL
10-06-2024 £2.49  Sid Meier’s Civilization VI
------------------------------
Subtotal by year
------------------------------
2023: £123.45
2024: £123.45
2025: £123.45
=============================
Total spend: £1234.56
=============================
```

## How to use:

1. Sign in to PlayStation in a web browser
2. Go to https://web.np.playstation.com/api/graphql/v1/transact/transaction/history?limit=250&startDate=2018-01-01T00%3A00%3A00.000%2B0000&endDate=2025-12-31T16%3A54%3A59.663%2B0100&includePurged=false&transactionTypes=CREDIT,CYCLE_SUBSCRIPTION,DEBIT,DEPOSIT_CHARGE,DEPOSIT_VOUCHER,PRODUCT_PURCHASE,REFUND_PAYMENT_CHARGE,REFUND_PAYMENT_WALLET,VOUCHER_PURCHASE,WALLET_BALANCE_CONVERSION
  Note: you can increase the limit and change the date range in the query params. If hasMore: true in the response, do multiple requests
3. Download the JSON file response and put it into a top-level "./transactions" directory.
4. Run `python line-items.json`