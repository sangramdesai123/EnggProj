'''def s():
    print("hellow sangram")

def b(x,y):
    print(x+y)

def a():
    global q    #defieing global varibale
    print(q)
    q+=1       #if not declear as global give error q=6 below
    print(q)

q=6
for x in range(0,11):
    if x%2==0:
        s()
    elif x==3:
        b(x,x+1)
    else:
        print(x)
'''

#file reading and writing

#creating new file always 'w'
text='These is new Text to add into file\nAdding new line here!!\n'
saveFile=open('newFile.txt','w') #open file if not creat new file
saveFile.write(text)
saveFile.close()

#appending new text to existing file if file not present create new
newtext='\n Here is new text to append in file whithout earseing previce text'
appendFile=open('newFile.txt','a')
appendFile.write(newtext)
appendFile.close()

#reading created file using 'r'
text=open('newFile.txt','r')
readFile=text.read()
print(readFile)
