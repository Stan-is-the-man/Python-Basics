from math import ceil
serial = input()
lenght_of_serial = int(input())
lenght_of_break = int(input())

time_for_lunch = 0.125 * lenght_of_break
time_for_rest = 0.25 * lenght_of_break

total_time = lenght_of_serial + time_for_lunch + time_for_rest
diff = abs(lenght_of_break - total_time)
if total_time <= lenght_of_break:
    print(f"You have enough time to watch {serial} and left with {ceil(diff)} minutes free time.")

if total_time > lenght_of_break:
    print(f"You don't have enough time to watch {serial}, you need {ceil(diff)} more minutes.")