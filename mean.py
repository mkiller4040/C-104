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

for i in range(len(datalist)):
    val = datalist[i][2]
    weightArray.append(float(val))

heightArraySum = 0
weightArraySum = 0

for i in heightArray :
    heightArraySum = heightArraySum + i

for i in weightArray :
    weightArraySum = weightArraySum + i

heightMean = heightArraySum/len(heightArray)
weightMean = weightArraySum/len(weightArray)

print("Height Mean = ", heightMean)
print("Weight Mean = ", weightMean)