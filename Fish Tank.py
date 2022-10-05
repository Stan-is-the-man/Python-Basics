lenght = int(input())
witht = int(input())
height = int(input())
percent = float(input())

volume_m2 = lenght * witht * height
volume_l = volume_m2 * 0.001
bulk = 0.17

litres_needed = volume_l * (1 -bulk)

print(litres_needed)



