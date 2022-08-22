item = input()
town = input()
quantity = float(input())


if town == 'Sofia':
    if item == 'coffee':
        print(0.5 * quantity)
    elif item == 'water':
        print(0.80 * quantity)
    elif item == 'beer':
        print(1.20 * quantity)
    elif item == 'sweets':
        print(1.45 * quantity)
    elif item == 'peanuts':
        print(1.60 * quantity)

elif town == 'Plovdiv':
    if item == 'coffee':
        print(0.40 * quantity)
    elif item == 'water':
        print(0.70 * quantity)
    elif item == 'beer':
        print(1.15 * quantity)
    elif item == 'sweets':
        print(1.30 * quantity)
    elif item == 'peanuts':
        print(1.50 * quantity)

elif town == 'Varna':
    if item == 'coffee':
        print(0.45 * quantity)
    elif item == 'water':
        print(0.70 * quantity)
    elif item == 'beer':
        print(1.10 * quantity)
    elif item == 'sweets':
        print(1.35 * quantity)
    elif item == 'peanuts':
        print(1.55 * quantity)