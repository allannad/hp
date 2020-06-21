#Load up the text of the books
import urllib.request
import requests
from bs4 import BeautifulSoup # note that the import package command is `bs4`
import requests
import lxml.html as lh
import pandas as pd

#----------------------------------------------------------------------
#parse through website to find all spells
#credit: https://towardsdatascience.com/web-scraping-html-tables-with-python-c9baba21059
#----------------------------------------------------------------------

url='https://www.pojo.com/harry-potter-spell-list/'
#Create a handle, page, to handle the contents of the website
page = requests.get(url)
#Store the contents of the website under doc
doc = lh.fromstring(page.content)
#Parse data that are stored between <tr>..</tr> of HTML
tr_elements = doc.xpath('//tr')
#print([len(T) for T in tr_elements[:12]])

tr_elements = doc.xpath('//tr')
#Create empty list
col=[]
i=0
#For each row, store each first element (header) and an empty list
for t in tr_elements[0]:
    i+=1
    name=t.text_content()
    #print('%d:"%s"'%(i,name))
    col.append((name,[]))

#Since the first row is the header, data is stored on the second row onwards
for j in range(1,len(tr_elements)):
    #T is our j'th row
    T=tr_elements[j]
    
    #If row is not of size 3, the //tr data is not from our table 
    if len(T)!=3:
        break
    
    #i is the index of our column
    i=0
    
    #Iterate through each element of the row
    for t in T.iterchildren():
        data=t.text_content() 
        #Check if row is empty
        if i>0:
        #Convert any numerical value to integers
            try:
                data=int(data)
            except:
                pass
        #Append the data to the empty list of the i'th column
        col[i][1].append(data)
        #Increment i for the next column
        i+=1
#print([len(C) for (title,C) in col])
Dict={title:column for (title,column) in col}
df=pd.DataFrame(Dict)
#Create spell list from Incantation column
spelllist = df['Incantation'].tolist()

#----------------------------------------------------------------------
#Create variables for the books by iterating through list of URLS
#----------------------------------------------------------------------

URLS = [
    "http://www.glozman.com/TextPages/Harry%20Potter%201%20-%20Sorcerer's%20Stone.txt",
    "http://www.glozman.com/TextPages/Harry%20Potter%202%20-%20Chamber%20of%20Secrets.txt",
    "http://www.glozman.com/TextPages/Harry%20Potter%203%20-%20The%20Prisoner%20Of%20Azkaban.txt",
    "http://www.glozman.com/TextPages/Harry%20Potter%204%20-%20The%20Goblet%20Of%20Fire.txt",
    "http://www.glozman.com/TextPages/Harry%20Potter%205%20-%20Order%20of%20the%20Phoenix.txt",
    "http://www.glozman.com/TextPages/Harry%20Potter%206%20-%20The%20Half%20Blood%20Prince.txt",
    "http://www.glozman.com/TextPages/Harry%20Potter%207%20-%20Deathly%20Hollows.txt"
]

booklist = []
for i in URLS:
    f = urllib.request.urlopen(i)
    book = f.read()
    book = str(book)
    booklist.append(book)
    #print(type(book))

#print(booklist[0])

#----------------------------------------------------------------------
#PICK SPELL TO VISUALIZE 
#----------------------------------------------------------------------

spell = input("Which spell would you like to count?", )
if spell not in spelllist:
    print("Invalid Spell")

