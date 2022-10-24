qt_packs_of_pens = int(input())
qt_packs_of_markers = int(input())
qt_litres_detergent = int(input())
discount = int(input())

total_pens = qt_packs_of_pens * 5.8
total_markers = qt_packs_of_markers * 7.2
total_detergent = qt_litres_detergent * 1.2

discount_in_number = discount / 100
total_without_discount = (total_pens + total_markers + total_detergent)

total_amount = total_without_discount - ((total_without_discount) * discount_in_number)


print(total_amount)
