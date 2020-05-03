def multiplied_by(num):
    for i in range(num,10*num,num):
        print(i)

number=input("Enter a number to get his table : ")
multiplied_by(int(number))
