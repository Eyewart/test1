"""DNA chain is a compound of a,t,g,c
-checking if the chain is valid
-typing the chain
-calculate the proportion"""

def EnterValue():
    string=input("Please enter the value: ")
    return string

def CheckValid(string):
    list=string.split()
    test=False
    for i in list:
        if i not in ("a", "c", "t", "g"):
            test=True
    return test

def CalcProp(string, seq):
    occ=string.count(seq)
    prop=len(seq)/len(string)
    return prop*occ*100

print("Please enter the DNA chain: \n")
str=EnterValue()
print("Please enter the sequence: \n")
seq=EnterValue()
print(CheckValid(str))
print("{} %".format(CalcProp(str, seq)))