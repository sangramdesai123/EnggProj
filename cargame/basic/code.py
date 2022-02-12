'''i want to get all href info from table in codechef page'''
import urllib.request
import urllib.parse
import re
#from BeautifulSoup import BeautifulSoup
from bs4 import BeautifulSoup
url='https://www.codechef.com/COOK93B'
#url for serch website link


html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, "html.parser")
print(html)
##for link in soup.findAll("<a>"):
##    print link.get("href")
    
#print(respData)     #printing data

'''these code give  full website html'''
##req=urllib.request.Request(url)#making request here
##
##resp=urllib.request.urlopen(req) #request the website to get data From web page
##
##respData=resp.read()    #read all data and store into varible
##
##print(respData)     #printing data

'''*************************************************************************'''
#parseing only paragrap from above website 
##
##paragraphs=re.findall(r'<p>(.*?)</p>',str(respData))
##
##for eachP in paragraphs:
##    print(eachP)
##
##print("hello")
