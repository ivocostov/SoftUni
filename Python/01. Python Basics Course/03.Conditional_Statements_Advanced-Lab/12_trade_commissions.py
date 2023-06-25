town = input()
sales = float(input())
sales_commission = 0
error = False

if town == 'Sofia':
    if 0 <= sales <= 500:
        sales_commission = sales * 0.05
    elif 500 < sales <= 1000:
        sales_commission = sales * 0.07
    elif 1000 < sales <= 10000:
        sales_commission = sales * 0.08
    elif sales > 10000:
        sales_commission = sales * 0.12
    else:
        error = True
elif town == 'Varna':
    if 0 <= sales <= 500:
        sales_commission = sales * 0.045
    elif 500 < sales <= 1000:
        sales_commission = sales * 0.075
    elif 1000 < sales <= 10000:
        sales_commission = sales * 0.10
    elif sales > 10000:
        sales_commission = sales * 0.13
    else:
        error = True
elif town == 'Plovdiv':
    if 0 <= sales <= 500:
        sales_commission = sales * 0.055
    elif 500 < sales <= 1000:
        sales_commission = sales * 0.08
    elif 1000 < sales <= 10000:
        sales_commission = sales * 0.12
    elif sales > 10000:
        sales_commission = sales * 0.145
    else:
        error = True
else:
    error = True

if error is False:
    print(f"{sales_commission:.2f}")
else:
    print('error')


