number_of_days = int(input())
number_of_hours = int(input())
total_tax = 0
for x in range(1, number_of_days + 1):
    tax_for_the_day = 0
    for z in range(1, number_of_hours + 1):
        if x % 2 == 0 and z % 2 != 0:
            tax_for_the_day += 2.50
            total_tax += 2.50
        elif x % 2 != 0 and z % 2 == 0:
            tax_for_the_day += 1.25
            total_tax += 1.25
        else:
            tax_for_the_day += 1
            total_tax += 1
    print(f'Day: {x} - {tax_for_the_day:.2f} leva')
print(f'Total: {total_tax:.2f} leva')