# leap year
# in theory a year is comprised of 365,25 days
# that's why every 4 years in february there is 29 days instead of 28
# this trick allows to compensate the missing day
# thus a leap year is comprised of 366 days instead of 365
# if a year is divided by 4 then it's a leap year

entered_year=input("Please choose a year:")
division_rest_4=int(entered_year)%4
division_rest_400=int(entered_year)%400
division_rest_100=int(entered_year)%100

if division_rest_4==0:
    if division_rest_100==0:
        if division_rest_400==0:
            print(int(entered_year), " is a leap year")
        else:
            print(int(entered_year), " is NOT a leap year")
    else:
        print(int(entered_year), " is a leap year")
else:
    print(int(entered_year), " is NOT a leap year")


