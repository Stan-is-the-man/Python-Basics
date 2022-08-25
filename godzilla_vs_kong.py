movie_budget = float(input())
number_of_statists = int(input())
price_per_cloth_for_1_statist = float(input())

expence_decor: float = movie_budget * 0.1
expence_clothes = number_of_statists * price_per_cloth_for_1_statist

if number_of_statists > 150:
    expence_clothes *= 0.9

total_expences = expence_decor + expence_clothes

difference = abs(total_expences - movie_budget)

if total_expences > movie_budget:
    print("Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")

elif total_expences <= movie_budget:
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")
