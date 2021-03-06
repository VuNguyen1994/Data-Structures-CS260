#Mark Boady
#Drexel University
#CS 260 - Summer 2020

# Name: Dinh Nguyen

#Time Two Sorts
import random
import timeit

def test_a_josephus(josephus_name,n):
	setup="from josephus_functions import "+josephus_name+"\n"
	setup+="n="+str(n)+"\n"
	setup+="m=2\n"
	test_code=josephus_name+"(n,m)"
	t=timeit.timeit(test_code,setup,number=1000)
	return t

print ("\nUsing M=2 and Number=? in timeit")	
print("  N  | List Ver. | Deque Ver. ")
for x in range(0,11):
	listver=test_a_josephus("josephus_list",2**x)
	dequever=test_a_josephus("josephus_deque",2**x)
	print("%4d |%10.5f |%10.5f"%(2**x,listver,dequever))
