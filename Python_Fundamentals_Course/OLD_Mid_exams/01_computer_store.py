total_order_price = 0
total_taxes = 0
total_price_with_taxes = 0
command = input()
while True:

    if command == "regular":
        if total_order_price == 0:
            print("Invalid order!")
            break
        total_price_with_taxes = total_order_price + total_taxes
        print("Congratulations you've just bought a new computer!")
        print(f"Price without taxes: {total_order_price:.2f}$")
        print(f"Taxes: {total_taxes:.2f}$")
        print("-----------")
        print(f"Total price: {total_price_with_taxes:.2f}$")
        break

    if command == "special":
        if total_order_price == 0:
            print("Invalid order!")
            break
        total_price_with_taxes = total_order_price + total_taxes
        discount = total_price_with_taxes * 0.1
        total_price_with_taxes -= discount
        print("Congratulations you've just bought a new computer!")
        print(f"Price without taxes: {total_order_price:.2f}$")
        print(f"Taxes: {total_taxes:.2f}$")
        print("-----------")
        print(f"Total price: {total_price_with_taxes:.2f}$")
        break
    if float(command) < 0:
        print("Invalid price!")
        command = input()
        continue

    total_order_price += float(command)
    total_taxes += float(command) * 0.2

    command = input()
