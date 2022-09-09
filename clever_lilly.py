age = int(input())
washing_machine_price = float(input())
price_per_toy = int(input())

toys = 0
money = 0
step = 5 # моя измислица, работи :)))))
sum_of_toys = 0
total_sum = 0

for num in range(1, age + 1):
    if num % 2 == 0:
        money = ((num * step) + money) - 1
    else:
        toys += 1

total_sum = money + (toys * price_per_toy)
diff = abs(total_sum - washing_machine_price)

if total_sum >= washing_machine_price:
    print(f'Yes! {diff:.2f}')
else:
    print(f'No! {diff:.2f}')