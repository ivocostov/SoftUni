sum_of_deposit = float(input())
months_of_deposit = int(input())
annual_interest_percentage = float(input())
annual_interest_sum = sum_of_deposit * annual_interest_percentage/100
annual_interest_for_a_month = annual_interest_sum/12
total_interest_for_user_inputed_months = months_of_deposit*annual_interest_for_a_month

sum_to_be_received_at_period_end = sum_of_deposit + total_interest_for_user_inputed_months
print(sum_to_be_received_at_period_end)