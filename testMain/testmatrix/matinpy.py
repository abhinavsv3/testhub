#seriation Problem
O=[1,2,3,4,5] #Data
d = []
[d.append([j-i for j in O]) for i in O]
print d