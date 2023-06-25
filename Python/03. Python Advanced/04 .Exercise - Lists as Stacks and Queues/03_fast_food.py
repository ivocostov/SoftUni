# from collections import deque
#
# initial_food_qty = int(input())
# orders_deque = deque(int(x) for x in input().split() if x.isdigit())
# biggest_order = max(orders_deque)

# for current_order in deque(orders_deque):
#     if orders_deque:
#         if current_order <= initial_food_qty:
#             orders_deque.popleft()
#             initial_food_qty -= current_order
#         else:
#             break
#     else:
#         break
#
# print(biggest_order)
# if orders_deque:
#     final_orders = []
#     for final in deque(orders_deque):
#         final_orders.append(str(final))
#     print(f"Orders left: {' '.join(final_orders)}")
# else:
#     print("Orders complete")


# ==============

from collections import deque

initial_food_qty = int(input())
orders_deque = deque(int(x) for x in input().split() if x.isdigit())
biggest_order = max(orders_deque)
print(biggest_order)

for order in orders_deque.copy():
    if initial_food_qty - order >= 0:
        orders_deque.popleft()
        initial_food_qty -= order
    else:
        print(f"Orders left: {' '.join([str(o) for o in orders_deque])}")
        break
else:
    print("Orders complete")