number = int(input())
counter = 1
is_bigger_than_number = False
for row in range(1, number + 1):
    for column in range(1, row + 1):
        if counter > number:
            is_bigger_than_number = True
            break
        print(counter, end=" ")
        counter += 1
    if counter > number:
        is_bigger_than_number = True
        break
    print()