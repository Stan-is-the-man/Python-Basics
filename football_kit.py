t_shirt_price = float(input())
target_sum = float(input())

short_price = 0.75 * t_shirt_price

socks_price = 0.20 * short_price

shoes_price = 2 * (t_shirt_price + short_price)

total_kit = (t_shirt_price + short_price + socks_price + shoes_price) * 0.85

diff = abs(total_kit - target_sum)
if total_kit >= target_sum:
    print('Yes, he will earn the world-cup replica ball!')
    print(f'His sum is {total_kit:.2f} lv.')
else:
    print('No, he will not earn the world-cup replica ball.')
    print(f'He needs {diff:.2f} lv. more.')