number_of_locations = int(input())

for x in range(number_of_locations):
    expected_avg_gold_per_day = float(input())
    number_of_days_for_this_location = int(input())
    total_mined = 0
    for z in range(number_of_days_for_this_location):
        gold_for_the_day = float(input())
        total_mined += gold_for_the_day


    if total_mined / number_of_days_for_this_location >= expected_avg_gold_per_day:
        print(f'Good job! Average gold per day: {total_mined / number_of_days_for_this_location:.2f}.')
    else:
        print(f'You need {expected_avg_gold_per_day - (total_mined / number_of_days_for_this_location):.2f} gold.')





