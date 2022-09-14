movie_name = input()
student_ticket = 0
standard_ticket = 0
kid_ticket = 0
total_sold_tickets = standard_ticket + student_ticket + kid_ticket

while movie_name != 'Finish':
    available_seats = int(input())
    type == movie_name
    sold_tickets = 0
    while type != 'End':
        available_seats_are_done = False
        if available_seats - sold_tickets == 0:
            available_seats_are_done = True
            break
        type_of_ticket = input()
        sold_tickets += 1
        if type_of_ticket == "student":
            student_ticket += 1
        elif type_of_ticket == 'standard':
            standard_ticket += 1
        elif type_of_ticket == 'kid':
            kid_ticket += 1
        print(f'{movie_name} - {total_sold_tickets / available_seats * 100}% full.')
    movie_name = input()


print(f'Total tickets: {total_sold_tickets}')
print(f'{student_ticket / total_sold_tickets * 100}% student tickets.')
print(f'{standard_ticket / total_sold_tickets * 100}% standard tickets.')
print(f'{kid_ticket / total_sold_tickets * 100}% kids tickets.')