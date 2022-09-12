name = input()
points_from_academy = float(input())
jury_members = int(input())

points = 0
total_points = 0
current_points = 0
for x in range(jury_members):
    jury_member_name = input()
    points_given = float(input())
    points += (len(jury_member_name) * points_given) / 2
    current_points = points + points_from_academy
    if current_points > 1250.5:
        break
if current_points > 1250.5:
    print(f'Congratulations, {name} got a nominee for leading role with {current_points:.1f}!')
elif current_points <= 1250.5:
    diff = abs(1250.5 - current_points)
    print(f'Sorry, {name} you need {diff:.1f} more!')






