vegetables_price = float(input())
fruits_price = float(input())
vegetables_quantity_in_kilos = float(input())
fruits_quantity_in_kilos = float(input())
euro = 1.94

total_vegetables_price_in_lv = vegetables_quantity_in_kilos * vegetables_price
total_fruits_price_in_lv = fruits_quantity_in_kilos * fruits_price

vegetables_profit_in_euro = total_vegetables_price_in_lv / euro
fruits_profit_in_euro = total_fruits_price_in_lv / euro

total_profit_in_euro = vegetables_profit_in_euro + fruits_profit_in_euro
print("{:.2f}".format(total_profit_in_euro))




