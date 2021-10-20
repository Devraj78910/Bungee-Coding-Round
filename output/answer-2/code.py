
import pandas as pd

from csv import writer
	
df = pd.read_csv("input\question-2\main.csv")

df1 = df[['occupation','age']]

occu = df.occupation.unique().tolist()

head = ['occupation','Min',"max"]
max = df1.groupby(['occupation']).max()
min = df1.groupby(['occupation']).min()

dfMax_list= max.values.tolist()
dfMin_list= min.values.tolist()

maxList = [i[0] for i in dfMax_list]
minList = [i[0] for i in dfMin_list]

print(minList)
with open('output\\answer-2\\main.csv', 'w', newline='') as file:
    writer_object = writer(file)
    writer_object.writerow(head)
    for item in enumerate(occu):
        i = item[0]
        writer_object.writerow([occu[i],minList[i],maxList[i]])
    file.close()