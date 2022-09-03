number_of_kozunak = int(input())
number_of_egg_cartons = int(input())
kg_kurabii = int(input())

price_for_kozunak = 3.2 * number_of_kozunak
price_for_egg_carton = 4.35 * number_of_egg_cartons
price_for_kurabii = 5.4 * kg_kurabii
price_for_egg_paint = 0.15 * number_of_egg_cartons * 12

total = price_for_egg_paint + price_for_kurabii + price_for_kozunak + price_for_egg_carton
print(f'{total:.2f}')