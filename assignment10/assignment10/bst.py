
#Mark Boady
#CS 260
#Binary Search Tree w/ Pointers
# Name: Dinh Nguyen
# CS 260
class node:
    def __init__(self,v,l=None,r=None):
        self.value = v
        self.left = l
        self.right = r
    def __str__(self):
        return str(self.value)
    def getValue(self):
        return self.value
    def setValue(self,v):
        self.value=v
    def getLeft(self):
        return self.left
    def setLeft(self,l):
        self.left = l
    def getRight(self):
        return self.right
    def setRight(self,r):
        self.right = r

class BST:
    def __init__(self):
        self.root=None
    def __str__(self):
        return self.inorder()
    #ADT Interface
    #These don't do much. They just set the correct inputs.
    def getRoot(self):
        return self.root
    def insert(self,value):
        self.root = self.insert_value(value, \
            self.root)
    def find(self,value):
        return self.find_value(value,self.root)
    def delete(self,value):
        self.root=self.delete_value(value, \
            self.root)
    def min(self):
        return self.find_min(self.getRoot())
    def inorder(self):
        return self.inorder_walk(self.root)
    def preorder(self):
        return self.preorder_walk(self.root)
    def postorder(self):
        return self.postorder_walk(self.root)
    def height(self):
        return self.node_height(self.root)
    #Recursive definition for insert
    def insert_value(self,value,mynode):
        #Implement me
        if mynode == None:
            return node(value)
        elif mynode.getValue() == value:
            return mynode
        elif mynode.getValue() > value:
            mynode.setLeft(self.insert_value(value,mynode.getLeft()))
        else:
            mynode.setRight(self.insert_value(value,mynode.getRight()))
        return mynode
    #Search Function
    def find_value(self,value,mynode):
        #Implement Me
        if mynode == None:
            return False
        elif mynode.getValue() == value:
            return True
        elif mynode.getValue() > value:
            return self.find_value(value,mynode.getLeft())
        else:
            return self.find_value(value,mynode.getRight())
        return None
    #Display Functions
    #Inorder Walk
    def inorder_walk(self,mynode):
        #Implement Me
        res = []
        def inorder_recur(mynode):
            if mynode == None:
                res.append("N")
            else:
                inorder_recur(mynode.getLeft())
                res.append(str(mynode.getValue()))
                inorder_recur(mynode.getRight())
        inorder_recur(mynode)
        return ' '.join(res)
    #Preorder Walk
    def preorder_walk(self,mynode):
        #Implement Me
        res = []
        def preorder_recur(mynode):
            if mynode == None:
                res.append("N")
            else:
                res.append(str(mynode.getValue()))
                preorder_recur(mynode.getLeft())
                preorder_recur(mynode.getRight())
        preorder_recur(mynode)
        return ' '.join(res)
    #Post Order
    def postorder_walk(self,mynode):
        #Implement Me
        res = []
        def postorder_recur(mynode):
            if mynode == None:
                res.append("N")
            else:
                postorder_recur(mynode.getLeft())
                postorder_recur(mynode.getRight())
                res.append(str(mynode.getValue()))
        postorder_recur(mynode)
        return ' '.join(res)
    #Delete From Tree
    #Recursive Definition (Works if you implement find min correctly)
    def delete_value(self,value,mynode):
        #Thing to delete not found
        if mynode==None:
            return None
        #Found Node to Delete
        elif mynode.getValue()==value:
            #If either side is null
            #Move up other side
            if mynode.getLeft()==None:
                return mynode.getRight()
            elif mynode.getRight()==None:
                return mynode.getLeft()
            #Otherwise reorganize!
            else:
                #Find Smallest Value on Right Side
                minval = self.find_min(\
                    mynode.getRight())
                #Swap to this position
                mynode.setValue(minval)
                #Remove that value
                #We know it has no left child
                new_right = self.delete_value(\
                    minval,mynode.getRight())
                #Update Pointers
                mynode.setRight(new_right)
                return mynode
        #Search More
        elif mynode.getValue() > value:
            mynode.setLeft(\
                self.delete_value(\
                    value,mynode.getLeft()))
            return mynode
        else:
            mynode.setRight(\
                self.delete_value(\
                    value,mynode.getRight()))
            return mynode
    #Find Min
    def find_min(self,mynode):
        #Implement Me
        if mynode == None:
            return None
        elif mynode.left == None:
            return mynode.getValue()
        else:
            return self.find_min(mynode.getLeft())
        return 0
    def node_height(self,mynode):
        #Implement Me
        if mynode == None:
            return -1
        leftH = self.node_height(mynode.getLeft())
        rightH = self.node_height(mynode.getRight())
        return 1 + max(leftH, rightH)



if __name__=="__main__":
    to_insert=[6,4,1,10,8,5,12]
    print("A simple set of BST Examples.")
    my_tree = BST()
    for x in to_insert:
        my_tree.insert(x)
        print("Tree After Insert "+str(x))
        print("Inorder:")
        print(my_tree.inorder())
        print("Preorder:")
        print(my_tree.preorder())
        print("Postorder:")
        print(my_tree.postorder())
    print("The height of the tree is",my_tree.height())
    for x in range(0,13):
        print("Is "+str(x)+" in the tree? "+str(my_tree.find(x)))
    for x in to_insert:
        my_tree.delete(x)
        print("Inorder after deleting "+str(x))
        print(my_tree.inorder())

