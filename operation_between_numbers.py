n1 = int(input())
n2 = int(input())
operator = input()

result = 0

if operator == '+':
    result = n1 + n2
elif operator == '-':
    result = n1 - n2
elif operator == '*':
    result = n1 * n2
elif operator == '/':
    if n2 == 0:
        print(f'Cannot divide {n1} by zero')
    else:
        result = n1 / n2
elif operator == '%':
    if n2 == 0:
        print(f'Cannot divide {n1} by zero')
    else:
        result = n1 % n2

even_or_odd = result % 2
value_even_odd = ''

if even_or_odd == 0:
    value_even_odd = 'even'
elif even_or_odd != 0:
    value_even_odd = 'odd'

if operator == '+' or operator == '-' or operator == "*":
    print(f'{n1} {operator} {n2} = {result} - {value_even_odd}')
elif operator == '/' and n2 != 0:
        print(f'{n1} / {n2} = {result:.2f}')
elif operator == '%' and n2 != 0:
        print(f'{n1} % {n2} = {result}')
