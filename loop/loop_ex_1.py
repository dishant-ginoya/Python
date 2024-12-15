while True:
    try:
        limit = int(input('How Many transactions store :- '))
        break
    except ValueError as e:
        print (' ---- Please Enter Digit ----\n')

transactions = []
result = {}

for i in range(limit):
    print()
    account_id = input('Enter Account Number :- ').strip()

    while True:
        types = input('Credit for C and Debit for D :- ').lower().strip()
        if types == 'd' or types == 'c':
            break
        else:
            print('---- Please Enter Credit for C and Debit for D ---- \n')
            continue

    while True:
        try:
            amount = int(input('Enter amount for transactions :-  '))
            break
        except ValueError as e:
            print(' ---- Please Enter Digit ----\n')
    transactions.append({'account_id': account_id, 'type': 'credit' if types == 'c' else 'debit', 'amount': amount})


for trans in transactions:
    acc_id = trans['account_id']
    type = trans['type']
    amount = trans['amount']

    if acc_id in result:
        result[acc_id][type].append(amount)
        result[acc_id]['balance'] = result[acc_id]['balance'] - amount if type == 'debit' else result[acc_id]['balance'] + amount
    else:
        if type == 'credit':
            result[acc_id] = {'balance': amount, 'debit': [], 'credit': [amount]}
        else:
            result[acc_id] = {'balance': 0 - amount, 'debit': [amount], 'credit': []}

print(result)
