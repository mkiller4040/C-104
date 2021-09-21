import csv, statistics

with open("height-weight.csv", newline = "") as f :
    reader = csv.reader(f)
    datalist = list(reader)

datalist.pop(0)

heightArray = []
weightArray = []

for i in range(len(datalist)) :
    val = datalist[i][1]
    heightArray.append(float(val))

for i in range(len(datalist)):
    val = datalist[i][2]
    weightArray.append(float(val))

heightMode = statistics.mode(heightArray)
weightMode = statistics.mode(weightArray)

print("Height Mode = ", heightMode)
print("Weight Mode = ", weightMode)
