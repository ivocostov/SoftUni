from collections import deque


def ramen_shop(number_of_ramen, number_of_customers):
    number_of_ramen, number_of_customers = deque(bowls_of_ramen), deque(customers)

    while number_of_ramen and number_of_customers:
        ramen_value = int(number_of_ramen.pop())
        customer_value = int(number_of_customers.popleft())

        if ramen_value > customer_value:
            result = ramen_value - customer_value
            number_of_ramen.append(str(result))

        elif ramen_value < customer_value:
            result = customer_value - ramen_value
            number_of_customers.appendleft(str(result))


    if not number_of_customers and not number_of_ramen:
        return f"Great job! You served all the customers."

    elif not number_of_customers:
        return f"Great job! You served all the customers.\nBowls of ramen left: {', '.join(number_of_ramen)}"

    elif not number_of_ramen:
        return f"Out of ramen! You didn't manage to serve all customers.\nCustomers left: {', '.join(number_of_customers)}"




bowls_of_ramen = input().split(', ')
customers = input().split(', ')

print(ramen_shop(bowls_of_ramen, customers))





