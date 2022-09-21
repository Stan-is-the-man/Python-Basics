favourite_book = input()
new_book = input()
counter = 0

while new_book != 'No More Books':
    if new_book == favourite_book:
        print(f'You checked {counter} books and found it.')
        break

    counter += 1
    new_book = input()

if new_book == 'No More Books':
    print('The book you search is not here!')
    print(f'You checked {counter} books.')