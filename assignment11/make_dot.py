#Mark Boady - CS260
# Name: Dinh Nguyen
# CS 260

# README: Making .dot of bst from input
# To run: enter a number sequence with space seperated
# enter a  <filename>.dot file name to store the graphic data of BST
# Compile the .dot file to create graph: dot -Tjpg -oexample1.jpg example1.dot
# Or run: bash test_dot.sh to run the test on make_dot.py

from bst import *

print ("Enter list of intergers (space seperated):")
seq = input()
print (seq)
print ("Enter Target file (some.dot):")
filename = input()
print (filename)

#check format input

#Insert a list into a tree
def make_tree(L):
    T=BST()
    for x in L:
        T.insert(x)
    return T

nodes = seq.split(' ')
T = make_tree(nodes)
dotfile = open(filename, "w")
dotfile.write("digraph {\n")

def write_node(mynode, parent,isRightNull): # isRightNull = 1 if right null, 0 if left null
    if mynode == None and isRightNull == False:
        dotfile.write("\tnode_null_l_"+str(parent)+" [label=\"Null\", shape=none];\n")
    elif mynode == None and isRightNull == True:
        dotfile.write("\tnode_null_r_"+str(parent)+" [label=\"Null\", shape=none];\n")
    else:
        dotfile.write("\tnode_"+str(mynode.getValue())+" [ label=\"" + str(mynode.getValue()) + "\"];\n")
        parent = mynode.getValue()
        if mynode.getLeft() == None:
            isRightNull = False
        write_node(mynode.getLeft(), parent, isRightNull)
        if mynode.getRight() == None:
            isRightNull = True
        write_node(mynode.getRight(), parent, isRightNull)

def write_edge(mynode, parent, isRightNull):
    if mynode == None and isRightNull == False:
        dotfile.write("\tnode_"+str(parent)+" -> node_null_l_"+str(parent)+";\n")
    elif mynode == None and isRightNull == True:
        dotfile.write("\tnode_"+str(parent)+" -> node_null_r_"+str(parent)+";\n")
    else:
        if parent != None:
            dotfile.write("\tnode_"+str(parent)+" -> node_"+str(mynode.getValue())+";\n")
        parent = mynode.getValue()
        if mynode.getLeft() == None:
            isRightNull = False
        write_edge(mynode.getLeft(),parent,isRightNull)
        if mynode.getRight() == None:
            isRightNull = True
        write_edge(mynode.getRight(),parent,isRightNull)
        
write_node(T.getRoot(), None, None)
write_edge(T.getRoot(), None, None)
dotfile.write("}")

dotfile.close()
print ("Dot Code saved in %s\n" % (filename))