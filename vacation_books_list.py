number_of_pages = int(input())
pages_done_for_one_hour = int(input())
number_of_days = int(input())

total_time_for_reading = number_of_pages / pages_done_for_one_hour

needed_hours_per_day = total_time_for_reading / number_of_days
from math import floor

print(floor(needed_hours_per_day))


