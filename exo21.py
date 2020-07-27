"""an integer 'n' between 2 and 12
the program gives how many ways are possible to reach this number with two dices"""

def CalculComb(numb):
    count = 0
    for x in range(1, 6):
        for y in range(1, 6):
            if x + y == numb:
                count += 1
    return count

end=False
while end is not True:
    numb_chosen=int(input("Please enter a number between 2 and 12: "))
    if numb_chosen>2 or numb_chosen<12:
        end=True

print("Number of combinations is: {}".format(CalculComb(numb_chosen)))

