import matplotlib.pyplot as plt

x=[1,2,3,4,5,6,7,8]
y=[1,2,3,4,5,6,7,8]

x2=[3,4,1,2,8,9,10,12]
y2=[1,5,6,7,6,2,10,12]

''' Label is not complusary in line plots '''

#plt.plot(x,y,label='First')   #making straight line from x,y list
#plt.plot(x2,y2,label='Second') #another graph

''' Makoing bar graphs label and color not cumplusary  '''

#plt.bar(x,y,label='BarChast 1',color='r')
#plt.bar(x2,y2,label='BarChast 2',color='c')

''' Historagram '''

#population=[22,55,33,98,42,11,55,66,44,10]
#bins=[0,10,20,30,40,50,60,70,80,90] #bins are required for histgram

#plt.hist(population,bins,histtype='bar',rwidth=0.8)#rwidth for making space between two bars


''' Scatter plot for corelation and regrations'''
#plt.scatter(x2,y2,label='skit')

''' stack plot '''
##days=[1,2,3,4,5]
##
##sleeping=[7,8,6,11,7]
##eating=[2,3,4,3,2]
##working=[7,8,7,2,2]
##playiing=[8,5,7,8,13]
##
##plt.stackplot(days,sleeping,eating,working,playiing)

''' pie chart '''

slices=[7,2,3,12]
activity=['sleeping','eating','working','playing']
plt.pie(slices,labels=activity)

plt.xlabel('X axis') #adding x label
plt.ylabel('Y axis')    #adding y label
plt.title('Interisting graph') #adding tital for graph

plt.legend() #making title inside graph using lables
plt.show()
