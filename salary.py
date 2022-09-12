number_of_opened_tabs = int(input())
salary = int(input())
penalty_fee = 0

for num in range(number_of_opened_tabs):
    website = input()
    if website == 'Facebook':
        penalty_fee += 150
    elif website == 'Instagram':
        penalty_fee += 100
    elif website == 'Reddit':
        penalty_fee += 50
    else:
        penalty_fee += 0

diff = salary - penalty_fee

if salary <= penalty_fee:
    print(f'You have lost your salary.')
else:
    print(diff)
