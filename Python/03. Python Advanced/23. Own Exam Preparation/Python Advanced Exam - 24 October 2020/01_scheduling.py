from collections import deque

jobs = deque(int(x) for x in input().split(', '))
job_index = int(input())

jobs_indexes = {}
clock_cycles = 0

for index, num in enumerate(jobs):
    jobs_indexes[index] = num

sorted_cycles = sorted(jobs_indexes.items(), key=lambda x: x[1])

for cycle in sorted_cycles:
    if job_index != cycle[0]:
        clock_cycles += cycle[1]
    else:
        clock_cycles += cycle[1]
        break

print(clock_cycles)



