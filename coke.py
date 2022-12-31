amount = 50
while amount >= 0:
    print(f'Ammount due:{amount}')
    insert = int(input('Insert Coin:'))
    if insert == 25 or insert == 10 or insert == 5:
        amount -= insert
    if insert > amount:
        break
print(f'Change Owed:{abs(amount)} ')



