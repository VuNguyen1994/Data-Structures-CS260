#Name: Dinh Nguyen

#Drexel University 2020
#CS 260 - Hash Table Homework

import open_hash

def hash_init(table,size):
    # Generate a sequence of random numbers between 0 and 5n and insert them to the hash table
    R = open_hash.random_sequence(size)
    for x in R:
        table.insert(x)
    
def average_collision(hash_type, size):
    count = 0       # total collision counts for hashing 10 times
    for i in range(0,10):
        H = open_hash.OpenHash(size,hash_type)
        hash_init(H, size)
        count += H.get_collision()
    return count/10

if __name__ == '__main__':
    print("   n | Hash1 (Avg Rate) | Hash2 (Avg Rate) | Hash3 (Avg Rate) ")
    for n in range(1, 12):
        size = 2**n
        avg1 = average_collision(open_hash.hash1, size)
        avg2 = average_collision(open_hash.hash2, size)
        avg3 = average_collision(open_hash.hash3, size)
        print("%4d | %16.1f | %16.1f | %16.1f " % (size, avg1, avg2, avg3))