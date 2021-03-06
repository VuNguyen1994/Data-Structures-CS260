#Mark Boady CS 260 - Drexel University 2020

# Name: Dinh Nguyen

from collections import deque
#Josephus
#Implemented using the builtin list as the queue
def josephus_list(n,m):
	# 0, 1, 2, 3, 4, 5, 6 -> 1, 3, 5, 0, 4, 2, 6
	# -> 2, 5, 1, 6, 4, 0, 3
	Q = []
	for i in range(n):
		Q.append(i)
	results=[]
	while not (len(Q)==0):
		for k in range(m-1):
			Q.append(Q.pop(0))
		results.append(Q.pop(0))
	return results
	
#Implemented using the deque object from collections
def josephus_deque(n,m):
	Q = deque()
	for i in range(n):
		Q.append(i)
	results=[]
	while not (len(Q)==0):
		for k in range(m-1):
			Q.append(Q.popleft())
		results.append(Q.popleft())	
	return results

