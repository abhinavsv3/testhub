graph = {}
with open('text.txt') as f:
	for line in f:
		(key,val) = line.split()
		graph[int(key)] = int(val)
	print graph
