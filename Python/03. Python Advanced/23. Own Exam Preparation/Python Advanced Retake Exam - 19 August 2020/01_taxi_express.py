from collections import deque

list_of_customers = input().split(', ')
list_of_taxis = input().split(', ')

customers = deque(list_of_customers)
taxis = deque(list_of_taxis)

total_time_to_drive_customers = 0

for current_customer in range(len(customers)):
    while customers and taxis:
        time_to_drive_customer = customers.popleft()
        time_to_refill_taxi = taxis.pop()

        if int(time_to_refill_taxi) >= int(time_to_drive_customer):
            total_time_to_drive_customers += int(time_to_drive_customer)

        else:
            customers.appendleft(time_to_drive_customer)
    else:
        break


if not customers:
    print(f"All customers were driven to their destinations\n"
          f"Total time: {total_time_to_drive_customers} minutes")

else:
    print(f"Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join(customers)}")



