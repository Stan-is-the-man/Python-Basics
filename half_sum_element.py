import sys
n_number = int(input())

sum = 0
max_number = -sys.maxsize

for num in range(n_number):
    current_number: int = int(input())
    # СМЯТА СУМАТА НА ВСИЧКИ ИНПУТИ !!!!!!!!!!!
    sum += current_number
    if current_number > max_number:
        max_number = current_number

diff = abs((max_number) - (sum - max_number))

if max_number == sum - max_number:
        print('Yes')
        print(f'Sum = {max_number}')
else:
    print('No')
    print(f'Diff = {diff}')