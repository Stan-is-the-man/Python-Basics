start = int(input())
end = int(input())
magic_num = int(input())
counter = 0
magic_num_is_found = False
for x in range(start, end + 1):
    for y in range(start, end + 1):
        sum = x + y
        counter += 1
        if sum == magic_num:
            print(f'Combination N:{counter} ({x} + {y} = {magic_num})')
            magic_num_is_found = True
            break

    if magic_num_is_found:
        break


if sum != magic_num:
    print(f'{counter} combinations - neither equals {magic_num}')