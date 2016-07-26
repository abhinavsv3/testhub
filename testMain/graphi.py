import sys
class graph:
	"""Graph class for accepting graphs"""
	def __init__(self, file, type):
		#Initial Loading being done here
		try:
			g = {}
			print "Here"
			with open(file) as f:
				print "Here2"
				for line in f:
					(key,val) = line.split()
					g[int(key)] = int(val)
				self.go = g
		except Exception as e:
			print "Exception Occured", e
		print "Done Copy"

	def printg(self):
		print self.go

file = 'text.txt'
g = graph(file,1)
print "I am in the main"
g.printg()
print "I just printed some stuff"
