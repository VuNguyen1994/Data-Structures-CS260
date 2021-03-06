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


def quicksort(A):
	def Partition (numbers, i, k):
		l = 0
		h = 0
		midpoint = 0
		pivot = 0
		temp = 0
		done = False
		#Pick middle element as pivot
		midpoint = i + (k - i)//2
		pivot = numbers[midpoint]

		l = i
		h = k
		while not done:
			# Increment l while numbers[l] < pivot
			while numbers[l] < pivot:
				l+=1
			# Decrement h while pivot < numbers[h]
			while pivot < numbers[h]:
				h -= 1
			# If there are zero or one elements remaining,
			# all numbers are partitioned. Return h
			if l >= h:
				done = True
			else:
				#Swap numbers[l] and numbers[h],
				# update l and h
				temp = numbers[l]
				numbers[l] = numbers[h]
				numbers[h] = temp
				l += 1
				h -= 1
		return h

	def Quicksort(numbers, i, k):
		j = 0
		# Base case: If there are 1 or zero elements to sort,
		# partition is already sorted
		if i >= k:
			return
		# Partition the data within the array. Value j returned from partitioning is location of last element in low partition
		j = Partition(numbers, i, k)
		# Recursively sort low partition i to j and high partition j+1 to k
		Quicksort(numbers, i, j)
		Quicksort(numbers, j+1, k)
	
	Quicksort(A, 0, len(A)-1)
	return A


def mergesort(A):
	def Merge(numbers, i, j, k):
		mergedSize = k - i + 1		# Size of merged partition
		mergePos = 0 				# Position to insert merged number
		leftPos = 0 				# Position of elements in left partition
		rightPos = 0 				# Position of elements in right partition
		mergedNumbers = []			# Dynamically allocates temporary array for merged numbers
		for num in range(mergedSize): # Initialize the mergedNumbers array
			mergedNumbers.append(0)

		leftPos = i					# Initialize left partition position
		rightPos = j + 1 			# Initialize right partition position
		# Add smallest element from left or right partition to merged numbers
		while leftPos <= j and rightPos <= k:
			if numbers[leftPos] <= numbers[rightPos]:
				mergedNumbers[mergePos] = numbers[leftPos]
				leftPos+=1
			else:
				mergedNumbers[mergePos] = numbers[rightPos]
				rightPos+=1
			mergePos+=1
		# If left partition is not empty, add remaining elements to merged numbers
		while leftPos <= j:
			mergedNumbers[mergePos] = numbers[leftPos]
			leftPos+=1
			mergePos+=1
		# If right partition is not empty, add remaining elements to merged numbers
		while rightPos <= k:
			mergedNumbers[mergePos] = numbers[rightPos]
			rightPos+=1
			mergePos+=1
		# Copy merge number back to numbers
		for mergePos in range(mergedSize):
			numbers[i + mergePos] = mergedNumbers[mergePos]

	def MergeSort(numbers, i, k):
		j = 0
		if i < k:
			j = (i + k)//2 		# Find the midpoint in the partition
			# Recursively sort left and right partitions
			MergeSort(numbers, i, j)
			MergeSort(numbers, j + 1, k)
			# Merge left and right partition in sorted order
			Merge(numbers, i, j, k)
	
	MergeSort(A, 0, len(A) - 1)
	return A

