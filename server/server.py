#!/usr/bin/python           
import socket 
import os
import hashlib
import sys
import math
from os import walk

LOCATION = "/Users/vishrutmehta/Documents/5thsem/Cloud/Merkel_Tree/client/"
BUFFER_SIZE = 8

def establishConnection():
	s = socket.socket()         
	host = socket.gethostname() 
	port = 12345                
	s.bind((host, port))        
	s.listen(5)
	return s


def Hashfunc(string):
	return hashlib.md5(string).hexdigest()
    
def filesize(filename):
    return os.path.getsize(filename)

def divideFile(filename):
	l = []
	f = open(filename, "r")
	count = 0
	while True:
		count = count + 1
		if count == BUFFER_SIZE:
			i = f.read()
			l.append(i)
			break
		else:
			i = f.read(filesize(filename)/BUFFER_SIZE)
			l.append(i)	
	f.close()
	return l

def getParticularDataBlock(filename, n):
	n = n - BUFFER_SIZE + 1
	f = open(filename,"r")
	count = 0
	import pdb;pdb.set_trace()
	while True:
		count = count + 1
		if count == BUFFER_SIZE and count == n:
			import pdb;pdb.set_trace()
			i = f.read()
			ans = i
			l.append(i)
			break
		else:
			i = f.read(filesize(filename)/BUFFER_SIZE)
			if count == n:
				ans = i
			l.append(i)	
	f.close()
	return ans


class MerkleTree:
	def __init__(self):
		self.tree = {}

	def insertcall(self, new_list, n):
		#x = int((math.ceil(math.log(n,2))))
		#max_size = 2*int(math.pow(2, x)) - 1
		tree = {}
		self.Insert(new_list, 0, n-1, tree, 0)
		self.tree = tree
		return tree

	def Insert(self, new_list, ss, se, tree, si):
		if ss == se:
			tree[str(si)] = new_list[ss]
			#tree.insert(si, new_list[ss])
			return new_list[ss]

		mid = self.getmid(ss, se)
		tree[str(si)] = self.hashfunc(str(self.Insert(new_list, ss, mid, tree, (si*2) + 1)) + str(self.Insert(new_list, mid+1, se, tree, (si*2) + 2)))
		return tree[str(si)]

	def getmid(self, s, e):
		return s + ((e-s)/2)

	def show(self):
		return self.tree	

	def hashfunc(self, string):
	    return hashlib.md5(string).hexdigest()

if __name__ == "__main__":

	f = []
	for (dirpath, dirnames, filenames) in walk("."):
		f.extend(filenames)
		break

	Alldic = {}
	for j in f:
		l = divideFile(j)
		x = MerkleTree()
		#print l
	#print l
		new_l = []
		for i in l:
			new_l.append(Hashfunc(i))
	#print new_l
			x.insertcall(new_l, len(new_l))
			Alldic[j] = x.show()
			#Alldic[j]['hash'] = x.show()
		#for k in range(len(Alldic[j]['hash']) - BUFFER_SIZE, len(Alldic[j]['hash'])):
		#	Alldic[j]['block'] = 
	print Alldic
	s = establishConnection()
	client = sys.argv[1]
	# scp to client
	while True:
		print "Enter 'update <filename> to sync the updated file to the client or q for quitting:"
		#c, addr = s.accept()
		#print "Got a connection from ", addr
		myin = raw_input().split()
		if myin[0] == "q":
			break
		elif myin[0] == "update":
			filename = myin[1]
			#print "filename:", filename 
			l = divideFile(filename)
			#print l
			x = MerkleTree()
			d = {}

			new_l = []
			for i in l:
				new_l.append(Hashfunc(i))

			x.insertcall(new_l, len(new_l))
			d = x.show()
			#print d
			# send
			for i in range(len(d.keys()) - BUFFER_SIZE, len(d.keys())):
			#	print i
			#	print d[str(i)]
			#	print Alldic[str(filename)][str(i)]
				if d[str(i)] != Alldic[str(filename)][str(i)]:
					#scp and break
					ans = divideFile(filename)
					ans = ans[i - BUFFER_SIZE + 1]
			del Alldic[filename]
			Alldic[filename] = d
			print Alldic
			try:
				LOCATION = sys.argv[2]
			except IndexError:
				pass
			os.system("ssh " + client + " rm " + LOCATION + filename)
			os.system("scp " + filename + " " + client + ":" + LOCATION)
			print "DONE"
			#Alldic[myin[1]] = x.show


		else:
			print "Incorrect command"
	#c.close()	
	#print x.show()
