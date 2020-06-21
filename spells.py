#Load up the text of the books
import urllib.request
import potter_spells as potter


#url = "http://www.glozman.com/TextPages/Harry%20Potter%201%20-%20Sorcerer's%20Stone.txt"
#file = urllib.request.urlopen(url)
#
#for line in file:
#	decoded_line = line.decode()
#	print(decoded_line)
#

#
link = "http://www.glozman.com/TextPages/Harry%20Potter%201%20-%20Sorcerer's%20Stone.txt"
f = urllib.request.urlopen(link)
myfile = f.read()
print(type(myfile))
#print(myfile)

#print(str(myfile.find(b"Harry")))


x = str(myfile)
print(type(x))
print(x)

#spell = re.search("Harry",x)
#print(spell)
spell = input("Which spell would you like to count?", )
print(x.count(spell))


potter.find('Avada Kedavra')

#book1 = myfile.decode("utf-8").find("\r\n\r\n")
#print(type(book1))
#
#with open(link) as f:
#    lines = f.readlines()
#print(type(lines))