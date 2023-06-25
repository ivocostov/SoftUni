pen_packages = int(input())
marker_packages = int(input())
cleaning_detergent_bottles = int(input())
discount_percentage = int(input())

pen_packages_price = 5.80
marker_packages_price = 7.20
cleaning_detergent_bottles_price = 1.20

total_money_for_pens = pen_packages * pen_packages_price
discount_for_pens = total_money_for_pens * discount_percentage / 100
price_for_pens_after_discount = total_money_for_pens - discount_for_pens

total_money_for_markers = marker_packages * marker_packages_price
discount_for_markers = total_money_for_markers * discount_percentage / 100
price_for_markers_after_discount = total_money_for_markers - discount_for_markers

total_money_for_cleaning_detergent = cleaning_detergent_bottles * cleaning_detergent_bottles_price
discount_for_cleaning_detergent = total_money_for_cleaning_detergent * discount_percentage / 100
price_for_cleaning_detergent_after_discount = total_money_for_cleaning_detergent - discount_for_cleaning_detergent

#знака "\" пренася на нов ред, но за компилатора си остава един ред
total_money_needed = price_for_pens_after_discount + price_for_markers_after_discount \
                     + price_for_cleaning_detergent_after_discount

print(total_money_needed)