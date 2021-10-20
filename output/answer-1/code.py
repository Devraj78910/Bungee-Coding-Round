import csv
from csv import writer

with open('input\question-1\main.csv', 'r') as f:
    reader = csv.reader(f)
    
    col_list = next(reader) 
        

    rows, cols = (6, 12)
    arr = [[0 for i in range(cols)] for j in range(rows)]
    
    arr[0][0]=1960
    arr[1][0]=1970
    arr[2][0]=1980
    arr[3][0]=1990
    arr[4][0]=2000
    arr[5][0]=2010

    col = [None] * 12

    for row in reader:
        if(int(row[0])<=1969):
            for i in range(1,12):
                col[i] = int(row[i])
                arr[0][i]+=col[i]        
        
        elif((int(row[0])<=1979) & (int(row[0])>=1970) ):            
            for i in range(1,12):
                col[i] = int(row[i])
                arr[1][i]+=col[i]
        elif((int(row[0])<=1989) & (int(row[0])>=1980) ):
            for i in range(1,12):
                col[i] = int(row[i])
                arr[2][i]+=col[i]
        elif((int(row[0])<=1999) & (int(row[0])>=1990) ):
            for i in range(1,12):
                col[i] = int(row[i])
                arr[3][i]+=col[i]
        elif((int(row[0])<=2009) & (int(row[0])>=2000) ):
            for i in range(1,12):
                col[i] = int(row[i])
                arr[4][i]+=col[i]
        elif(int(row[0])>=2010):
            for i in range(1,12):
                col[i] = int(row[i])
                arr[5][i]+=col[i]
        
with open('output\\answer-1\\main.csv', 'w', newline='') as file:	
    writer_object = writer(file)
    writer_object.writerow(col_list)
    for i in range(6):
	    writer_object.writerow(arr[i])
    file.close()

	