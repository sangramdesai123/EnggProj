import matplotlib.pyplot as plt
import csv
with open('example.csv') as csvfile: #open csv file
    readCSV=csv.reader(csvfile,delimiter=',')#making object of csv file and cut it at '
    print(readCSV)

    for row in readCSV :#loop and print 
        print(row)#print all contain incsv
        print(row[0])

    dates=[]
    colors=[]
    for row in readCSV :#loop and print 
        date=row[0]
        color=row[3]

        dates.append(date)
        colors.append(color)

    print(dates)
    print(colors)

import numpy as np

''' ploting graphs using csv files using numpy '''
x,y = np.loadtxt('r.csv',delimiter=',',unpack=True)#for reading csv file
#x,y = np.loadtxt('r.txt',delimiter=',',unpack=True)#for reading text file
plt.plot(x,y,label='csv chart')

plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('reading csv in matplot')
plt.legend()
plt.show()


