pool_volume = int(input())
first_pipe_debit_per_hour = int(input())
second_pipe_debit_per_hour = int(input())
missing_hours_of_worker = float(input())

pool_volume_in_percentage = 100
total_debit_first_pipe = first_pipe_debit_per_hour * missing_hours_of_worker
total_debit_second_pipe = second_pipe_debit_per_hour * missing_hours_of_worker

total_debit_both_pipes = total_debit_first_pipe + total_debit_second_pipe

first_pipe_debit_in_percentage = total_debit_first_pipe / total_debit_both_pipes * 100
second_pipe_debit_in_percentage = total_debit_second_pipe / total_debit_both_pipes *  100

total_pipe_percentage = total_debit_both_pipes / pool_volume * 100
difference_in_liters = abs(pool_volume - total_debit_both_pipes)

if total_debit_both_pipes <= pool_volume:
    print(f"The pool is {total_pipe_percentage:.2f}% full. Pipe 1: {first_pipe_debit_in_percentage:.2f}%. \
Pipe 2: {second_pipe_debit_in_percentage:.2f}%.")
else:
    print(f"For {missing_hours_of_worker:.2f} hours the pool overflows with {difference_in_liters:.2f} liters.")
