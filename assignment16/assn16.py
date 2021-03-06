# Name: Dinh Nguyen
# Assignment16 Find the shortest path
# To run: python3 assn16.py 
# Fill in input file name
# Enter a command: help, exit (or Ctrl D) or dijkstra x

import sys
import heapq
import math

fname = input("File containing graph: ")
# Build adjacent matrix using input data
matrix = []
numNodes = 0
try:
    with open(fname, "r") as f:
        numNodes = int(f.readline())
        # init the graph matrix
        for i in range(0,numNodes):
            row = []
            for k in range(0,numNodes):
                row.append(math.inf)
            row[i] = 0.0
            matrix.append(row)
        for line in f:
            matrix[ int(line[0]) ][ int(line[2]) ] = float(line[4])
except Exception as err:
    sys.exit(err)

def Dijkstra(G, start_node):
    S = []
    S.append(start_node)
    D = []
    for x in range(0,numNodes):
        D.append(math.inf)
    D[start_node] = 0.0
    H = []
    for i in range(0,len(D)):
        heapq.heappush(H, [D[i],i])
    while H != []:
        u = H[0][1]
        S.append(u)
        heapq.heappop(H)  
        for v in range(0,numNodes):
            if G[u][v] > 0 and G[u][v] != math.inf:     #Adjacent edge
                if D[v] > D[u] + G[u][v]:
                    D[v] = D[u] + G[u][v]
                    #update Heap
                    H = []
                    for i in range(0,len(D)):
                        if i not in S:
                            heapq.heappush(H, [D[i],i])
    return D

# print menu and get cmd input
menu = "Possible Commands are: \ndijkstra x - Runs Dijkstra starting at node X. X must be an integer \nhelp - prints this menu \nexit or ctrl-D - Exits the program"
print(menu)
try:
    cmd = input("Enter command: ")
except Exception as err:
    print("\nBye")
    sys.exit(0)

# Handle cmds
while cmd != 'exit':
    if cmd == 'help':
        print(menu)
        try:
            cmd = input("Enter command: ")
        except Exception as err:
            print("\nBye")
            sys.exit(0)
    elif 'dijkstra' in cmd:
        startNode = int(cmd[9])
        print(Dijkstra(matrix,startNode))
        try:
            cmd = input("Enter command: ")
        except Exception as err:
            print("\nBye")
            sys.exit(0)
    else:
        print("Invalid command!!!", cmd)
        print(menu)
        try:
            cmd = input("Enter command: ")
        except Exception as err:
            print("\nBye")
            sys.exit(0)

if cmd == 'exit':
    print("Bye")
    sys.exit(0)  
    