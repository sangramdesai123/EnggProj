'''website scriping data from other websites somtims website
    like google block our code then use API provided by them
    or use HEADERS
    HEADER contains user agent pc information and all other
    required data
    for more information view sentdex tutorial on urllib
'''
import urllib.request
import urllib.parse
import re

url='https://pythonprogramming.net/machine-learning-tutorial-python-introduction'
#url for serch website link

req=urllib.request.Request(url)#making request here

resp=urllib.request.urlopen(req) #request the website to get data From web page

respData=resp.read()    #read all data and store into varible

#print(respData)     #printing data

'''*************************************************************************'''
#parseing only paragrap from above website 

paragraphs=re.findall(r'<p>(.*?)</p>',str(respData))

for eachP in paragraphs:
    print(eachP)
