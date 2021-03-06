#Mark Boady - CS 260
#Drexel University 2020

# Name: Dinh Nguyen

#Complete the Following Functions
def bubblesort(A):
	for i in range(0, len(A)):
		for j in range(0, len(A)-i-1):
			if A[j]>A[j+1]:
				temp = A[j]
				A[j] = A[j+1]
				A[j+1] = temp
	return A

def insertion(A):
	for i in range(1, len(A)):
		j = i
		while j>0 and A[j]<A[j-1]:
			#swap
			temp = A[j]
			A[j] = A[j-1]
			A[j-1] = temp
			j-= 1
	return A


def builtinsort(A):
	return A.sort()
