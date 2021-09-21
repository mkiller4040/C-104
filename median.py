import csv

with open("height-weight.csv", newline = "") as f :
    reader = csv.reader(f)
    datalist = list(reader)

datalist.pop(0)

heightArray = []
weightArray = []

for i in range(len(datalist)) :
    val = datalist[i][1]
    heightArray.append(float(val))

heightArray.sort()

length = int(len(heightArray)/2)

if (len(heightArray)%2 == 0) :
    median2 = heightArray[length]
    median1 = heightArray[length - 1]

    median = (median1 + median2)/2
else :
    median = heightArray[len(heightArray)/2]

print("Height Median = ", median)



