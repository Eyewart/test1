import calc_radius

r_cercle=calc_radius.Cercle(int(input("Please choose a value for the radius: ")))
print("Surface: ", r_cercle.calc_s())
print("Perimeter: ", r_cercle.calc_p())