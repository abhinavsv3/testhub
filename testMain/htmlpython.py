import math
from string import Template
import webbrowser

print "Hi Buddy!"
print "Who are you?"
st = raw_input(">>")

print "Hey "+st
temp = Template("<html><body><h1>Hi, Welcome to my world, ${name}, ${name}</h1></body></html>")
k = temp.substitute(dict(name = st))
print k
f = open("testhtml.html","w")
f.write(k)
f.close()


new = 2
url = "testhtml.html"
webbrowser.open(url,new=new)