import math
width = float(input())
length = float(input())
heigth = float(input())
avg_astronaut_heigth = float(input())

room_heigth = 0.4 + avg_astronaut_heigth
space_ship_volume = heigth * width * length
room_volume_for_1_austornaut = room_heigth * 2 * 2

spec = space_ship_volume / room_volume_for_1_austornaut
if 3 <= spec <= 10:
    print(f'The spacecraft holds {math.floor(spec)} astronauts.')
elif spec < 3:
    print('The spacecraft is too small.')
else:
    print('The spacecraft is too big.')




