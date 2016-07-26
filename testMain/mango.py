import webbrowser

print "Hi Buddy!"
print "Who are you?"
st = raw_input(">>")
url = "http://abhinavsv3.github.io/"
print "Hey "+st
new=2
while 1==1 :
	st = raw_input(">>")
	print st
	if st == "g":
		url = "https://www.google.co.in/"
	webbrowser.open(url,new=new)