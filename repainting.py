qt_pvc_cover = int(input())
littres_of_paint = int(input())
littres_of_amv = int(input())
working_hours = int(input())
additional_paint = littres_of_paint * 0.1

sum_pvc_cover = qt_pvc_cover * 1.5
sum_paint = littres_of_paint * 14.5
sum_amv = littres_of_amv * 5
sum_additional_paint = additional_paint * 14.5
sum_additional_pvc_cover = 2 * 1.5
sum_bags = 0.4

total_materials = sum_pvc_cover + sum_paint + sum_amv + sum_additional_paint + sum_additional_pvc_cover + sum_bags
labour_for_one_hour = total_materials * 0.3
sum_of_labour = working_hours * labour_for_one_hour
all_expenses = total_materials + sum_of_labour

print(all_expenses)
