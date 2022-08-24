type = input()
rows = int(input())
columns = int(input())

number_of_seats = rows * columns
total_income = 0

if type == 'Premiere':
    total_income = number_of_seats * 12.00
elif type == 'Normal':
    total_income = number_of_seats * 7.50
else:
    total_income = number_of_seats * 5.00

print(f'{total_income:.2f} leva')
