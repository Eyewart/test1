"""while : calculate price from HT to TTC
type o to get out of the loop"""

end=False
while end is not True:
    price_HT=input("What's the price in HT? Or press 'o' to terminate \n")
    if price_HT=="o":
        end=True
    else:
        price_TTC=int(price_HT)*1.21
        print(str(price_TTC))

