account_money = 0

while True:
    deposit = input()
    if deposit == 'NoMoreMoney':
        break

    current_deposit = float(deposit)

    if current_deposit < 0:
        print('Invalid operation!')
        break
    else:
        account_money += current_deposit
        print(f"Increase: {current_deposit:.2f}")

print(f"Total: {account_money:.2f}")
