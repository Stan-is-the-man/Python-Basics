figure = input()

if figure == 'square':
    side = float(input())
    surface_square = side * side
    print(f"{surface_square:.3f}")

elif figure == 'rectangle':
    side_a = float(input())
    side_b = float(input())
    surface_rec = side_a * side_b
    print(f"{surface_rec:.3f}")

elif figure == 'circle':
    radius = float(input())
    from math import pi
    surface_cir = (radius ** 2) * pi
    print(f"{surface_cir:.3f}")

elif figure == 'triangle':
    side_of_triangle = float(input())
    belonging_side_of_triangle = float(input())
    surface_tri = (side_of_triangle * belonging_side_of_triangle) / 2
    print(f"{surface_tri:.3f}"
