"""hunting license with points
each hunter has 100 points at start. if he kills he loose points:
1pt for chicken
3pt for dogs
5pt for cows
10pt for a friend
the license costs 200 euros
create a function 'amende' (nbr victime) = sum to spend"""

def CalculPoints(ch, d, c, f):
    capital=100
    points=capital-(1*ch+3*d+5*c+10*f)
    return points

chicken=int(input("How many chickens?"))
dogs=int(input("How many dogs?"))
cows=int(input("How many cows?"))
friends=int(input("How many friends?"))

pay=2*(CalculPoints(chicken,dogs,cows,friends))

if pay==0:
    print("nothing to pay. bye")
else:
    print("to pay: {}".format(str(pay)))

