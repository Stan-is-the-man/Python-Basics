flower_type = input()
flower_quantity = int(input())
budget = int(input())

expences = 0

if flower_type == 'Roses':
    if flower_quantity > 80:
        expences = flower_quantity * 5 * 0.90
    else:
        expences = flower_quantity * 5
elif flower_type == 'Dahlias':
    if flower_quantity > 90:
        expences = flower_quantity * 3.80 * 0.85
    else:
        expences = expences = flower_quantity * 3.80

elif flower_type == 'Tulips':
    if flower_quantity > 80:
        expences = flower_quantity * 2.80 * 0.85
    else:
        expences = flower_quantity * 2.80
elif flower_type == 'Narcissus':
    if flower_quantity < 120:
        expences = flower_quantity * 3 * 1.15
    else:
        expences = flower_quantity * 3
elif flower_type == 'Gladiolus':
    if flower_quantity < 80:
        expences = flower_quantity * 2.5 * 1.20
    else:
        expences = flower_quantity * 2.5


diff = abs(budget - expences)

if budget >= expences:
    print(f'Hey, you have a great garden with {flower_quantity} {flower_type} and {diff:.2f} leva left.')
else:
    print(f'Not enough money, you need {diff:.2f} leva more.')
