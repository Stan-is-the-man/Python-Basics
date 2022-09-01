import sys
number_of_kozunak = int(input())
command = ''
points = 0
max_points = -sys.maxsize
baker_with_max_points = ''
for x in range(number_of_kozunak):
    name_of_baker = input()
    command = input()
    while command != "Stop":

        points_from_one_person = int(command)
        points += points_from_one_person
        command = input()

    print(f'{name_of_baker} has {points} points.')
    if points > max_points:
        max_points = points
        baker_with_max_points = name_of_baker
        print(f'{name_of_baker} is the new number 1!')
    points = 0

print(f'{baker_with_max_points} won competition with {max_points} points!')

