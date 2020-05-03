def multiplied_by(num):
    i=0
    while i < 10:
        print(i+1, "*", num , "=" , (i+1) * num)
        i += 1

number=input("Enter a number to get his table")
multiplied_by(int(number))