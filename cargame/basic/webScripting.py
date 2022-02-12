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

url='http://pythonprogramming.net'       #url for serch website link

values={'s':'basics','submit':'search'}  #serching basic and clicking button on website

data=urllib.parse.urlencode(values)   #make encode data to parse into data

data=data.encode('utf-8')       #encode data into charater sequence from encode page data

req=urllib.request.Request(url,data)#making request here

resp=urllib.request.urlopen(req) #request the website to get data From web page

respData=resp.read()    #read all data and store into varible

#print(respData)     #printing data

'''*************************************************************************'''
#parseing only paragrap from above website 

paragraphs=re.findall(r'<p>(.*?)</p>',str(respData))

for eachP in paragraphs:
    print(eachP)
