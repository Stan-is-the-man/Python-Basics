city = input()
volume_of_sales = float(input())

bonus = 0

if city == 'Sofia':
    if 0 <= volume_of_sales <= 500:
        bonus = volume_of_sales * 0.05
        print(f'{bonus:.2f}')
    elif 500 < volume_of_sales <= 1000:
        bonus = volume_of_sales * 0.07
        print(f'{bonus:.2f}')
    elif 1000 < volume_of_sales <= 10000:
        bonus = volume_of_sales * 0.08
        print(f'{bonus:.2f}')
    elif volume_of_sales > 10000:
        bonus = volume_of_sales * 0.12
        print(f'{bonus:.2f}')
    else:
        print('error')

elif city == 'Varna':
    if 0 <= volume_of_sales <= 500:
        bonus = volume_of_sales * 0.045
        print(f'{bonus:.2f}')
    elif 500 < volume_of_sales <= 1000:
        bonus = volume_of_sales * 0.075
        print(f'{bonus:.2f}')
    elif 1000 < volume_of_sales <= 10000:
        bonus = volume_of_sales * 0.1
        print(f'{bonus:.2f}')
    elif volume_of_sales > 10000:
        bonus = volume_of_sales * 0.13
        print(f'{bonus:.2f}')
    else:
        print('error')

elif city == 'Plovdiv':
    if 0 <= volume_of_sales <= 500:
        bonus = volume_of_sales * 0.055
        print(f'{bonus:.2f}')
    elif 500 < volume_of_sales <= 1000:
        bonus = volume_of_sales * 0.08
        print(f'{bonus:.2f}')
    elif 1000 < volume_of_sales <= 10000:
        bonus = volume_of_sales * 0.12
        print(f'{bonus:.2f}')
    elif volume_of_sales > 10000:
        bonus = volume_of_sales * 0.145
        print(f'{bonus:.2f}')
    else:
        print('error')

else:
    print('error')