deposit = float(input())
term_of_deposit = int(input())
anual_interest_rate = float(input())

interest = deposit * (anual_interest_rate / 100)

monthly_interest = interest / 12





total_sum_at_the_end = deposit + (term_of_deposit * monthly_interest)



print(total_sum_at_the_end)
