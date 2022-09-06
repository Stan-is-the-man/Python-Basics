up_1 = int(input())
up_2 = int(input())
up_3 = int(input())

for a in range(1, up_1 + 1):
    number_is_ok = False
    if a % 2 == 0:
        number_is_ok = True

    for b in range(1, up_2 + 1):
        number_is_prime = False
        if b == 2 or b == 3 or b == 5:
            number_is_prime = True

        for c in range(1, up_3 + 1):
            number_is_fine = False
            if c % 2 == 0:
                number_is_fine = True

                if number_is_ok and number_is_fine and number_is_prime:
                    print(f'{a}{b}{c}')
