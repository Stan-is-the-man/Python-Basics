command = input()
sum_prime_nums = 0
sum_non_prime_nums = 0

while command != 'stop':
    current_number = int(command)
    if current_number < 0:
        print('Number is negative.')

    else:
        number_is_not_prime = False
        for x in range(2, current_number):
            if current_number % x == 0:
                number_is_not_prime = True
                break


        if number_is_not_prime:
            sum_non_prime_nums += current_number
        else:
            sum_prime_nums += current_number

    command = input()
print(f'Sum of all prime numbers is: {sum_prime_nums}')
print(f'Sum of all non prime numbers is: {sum_non_prime_nums}')


