list=[1,2,30,4,5,6,7,8,8,10,8]

list.append(0)#append to end of list
print(list)

list.insert(2,99)#insert at 2 position value 99
print(list)

list.remove(2)#remove first occurence of 2 in list
print(list)

print(list[1:])#slicing list from 1 to end
print(list[:2])#slicing list from 0 to 2
print(list[1:7])#slicing list from 1 to 7 index

print(list.index(30))#give the index of 30 in list
print(list.count(8)) #give count of frequency of 8 in list

list.sort()#sort given list ascending order
y=list  #copy entire list
x=list[1:5] #copy list from 1 to 5 index
print(x)
print(y)

'''multi-dimensional List'''
a=[[5,3],[3,2],[2,1]]#2d list
print(a[0])#print first row list
print(a[0][1]) #print 0 row 1 column value
print(a)
