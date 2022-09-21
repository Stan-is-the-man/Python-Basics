total = 0

while True:

    value = input()

    if value == 'NoMoreMoney':
        break
    elif float(value) < 0:
        print('Invalid operation!')
        break

    total += float(value)
    print(f'Increase: {float(value):.2f}')

print(f'Total: {total:.2f}')