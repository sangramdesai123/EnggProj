import statistics #as s
#u can use these as import statistics as s <<----

#then use function as
# y= s.mean(list)
list=[1,2,30,4,5,6,7,8,8,10]

y=statistics.mean(list)#finding mean in list
print(y)

y=statistics.median(list)#finding median in list
print(y)

y=statistics.mode(list)#mode maxium no of occurense of number 8 occure 2times
print(y)

y=statistics.stdev(list)#standerd deviation sqrt of varience
print(y)

y=statistics.variance(list)#varience square of stdev
print(y)
