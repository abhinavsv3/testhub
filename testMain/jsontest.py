import json as j
'''l = [1,2]
b = [2,3]
n = {"l":l,"b":b}
a = [n,n]
m = [n,n]
lp = {"a":a,"m":m}
k=j.dumps(lp,indent = 4)
print k
f = open('abc.json',"w")
f.write(k)
f.close()'''
with open("jj.json") as jf:
	jd = j.load(jf)
	#print jd
print "Nodes"
#print jd['nodes']

print "JD",type(jd)
print "Keys of JD"
for key,value in jd.iteritems():
	print key

print 
l = jd['nodes']
print type(l)
k = l[0]
print type(k)
print k['cluster']

