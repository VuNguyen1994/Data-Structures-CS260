#!/bin/python3

# Name: Dinh Nguyen - CS 260 Summer 2020

#The Normal Python Function
def pow1(a,b):
        return a**b
#Computes a^b (integers a,b)
#Only works for b >= 0
def pow2(a,b):
        total=1
        for i in range(0,b):
                total=total*a
        return total
#Computes a^b (integers a,b)
#Only works for b >= 0
def pow3(a,b):
        if b==0:
                return 1
        elif b%2==1:
                return a*pow3(a,b-1)
        else:
                temp=pow3(a,b//2)
                return temp*temp

if __name__ == '__main__':
	import timeit
	t_pow1 = [] 	# [2^1, 2^10, 2^100, 2^1000, 3^1, 3^10, 3^100, 3^1000, 4^1, 4^10, 4^100, 4^1000] 
	t_pow2 = []
	t_pow3 = []
	for base in range (2,5):
		for i in range(0, 4):
			k = 10**i
			t_pow1.append(timeit.timeit("pow1("+str(base)+","+str(k)+")",setup="from __main__ import pow1"))
			t_pow2.append(timeit.timeit("pow2("+str(base)+","+str(k)+")",setup="from __main__ import pow2"))
			t_pow3.append(timeit.timeit("pow3("+str(base)+","+str(k)+")",setup="from __main__ import pow3"))
	#print ("DEBUG: [2^1, 2^10, 2^100, 2^1000, 3^1, 3^10, 3^100, 3^1000, 4^1, 4^10, 4^100, 4^1000]")
	#print ("t_pow1:", t_pow1)
	#print ("t_pow2:", t_pow2)
	#print ("t_pow3:", t_pow3) 
	print ("OUTPUT")
	print ("  k  | pow1(2,k) | pow1(3,k) | pow1(4,k) | pow2(2,k) | pow2(3,k) | pow2(4,k) | pow3(2,k) | pow3(3,k) | pow3(4,k) \n")
	for idx in range(0,4):
		k = 10**idx
		print ("%4d | %9.6f | %9.6f | %9.6f | %9.6f | %9.6f | %9.6f | %9.6f | %9.6f | %9.6f" % (k, t_pow1[idx],t_pow1[idx+4],t_pow1[idx+8], t_pow2[idx], t_pow2[idx+4],t_pow2[idx+8], t_pow3[idx], t_pow3[idx+4], t_pow3[idx+8]))



