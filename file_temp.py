file=open("temperature.txt","w")

list_temp=["hot","cold","tempered","freezing"]

for t in list_temp:
    file.write(t + "\n")

file.close()