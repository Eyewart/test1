"""while the sum of positive numbers or equal to zero
it will count how many numbers entered and if the sum is superior to 100"""

end=False
sum=0
count=0
while end is not True:
    numb=input("Please enter a positive number (0 or negative number to end) : ")
    numb=int(numb)
    count+=1
    if numb <= 0:
        end=True
    else:
        sum+=numb
        print("There was {} numbers to sum and the total is equal to {}".format(count, sum))
