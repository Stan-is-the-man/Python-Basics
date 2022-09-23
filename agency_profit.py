company_name = input()
number_of_adult_tickets = int(input())
number_of_child_tickets = int(input())
net_price_of_adult_ticket = float(input())
tax_extra = float(input())


net_price_of_child_ticket = net_price_of_adult_ticket * 0.30 + tax_extra
net_price_of_adult_ticket += tax_extra
final_incomes = number_of_adult_tickets * net_price_of_adult_ticket \
                + number_of_child_tickets * net_price_of_child_ticket

final_profit = final_incomes * 0.2

print(f'The profit of your agency from {company_name} tickets is {final_profit:.2f} lv.')