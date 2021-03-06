# Name: Dinh Nguyen
# CS 260

from bst import *
import random

#Insert a list into a tree
def make_tree(L):
	T=BST()
	for x in L:
		T.insert(x)
	return T

def random_sequence(size):
	X=[x for x in range(0,5*size+1)]
	random.shuffle(X)
	return X[0:size]

print ("     n | Height(E1) | Height(E2) | Height(E3) | Height(E4) | Height(E5) | Height(AVG)")
for a in range(1,11):
    n = 2**a
    Heights = []
    for exp in range(0,5):
        L = random_sequence(n)
        T=make_tree(L)
        Heights.append(T.height())
        # print(L)
    Height_AVG = sum(Heights)/5.0
    print(" %5d | %10d | %10d | %10d | %10d | %10d | %10.1f" % (n, Heights[0], Heights[1], Heights[2], Heights[3], Heights[4], Height_AVG))