from collections import deque

q = deque()

#Enqueue, push, add
q.append(2)      # append to the right
q.appendleft(3)  # append to the left

#Dequeue, pop, remove

q.pop()      # pop from right
q.popleft()  # pop from left

#Peek
print(q[-1])

# Count