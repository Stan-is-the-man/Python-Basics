command = input()
total_days = 1
reached_meters = 5364
everest_is_reached = False
day_limit_is_reached = False
while command != "END":
    meters_for_today = int(input())

    if command == "Yes":
        total_days += 1
        reached_meters += meters_for_today
        if reached_meters >= 8848:
            everest_is_reached = True
            break
        if total_days == 6:
            day_limit_is_reached = True
            break
    elif command == "No":
        reached_meters += meters_for_today
        if reached_meters >= 8848:
            everest_is_reached = True
            break

    command = input()

if everest_is_reached:
    print(f'Goal reached for {total_days} days!')
elif day_limit_is_reached:
    print('Failed!')
    print(f'{reached_meters}')

else:
    print('Failed!')
    print(f'{reached_meters}')