class Node:
    def __init__(self,data=None):
        self.left = None
        self.right = None
        self.val = data
        self.parent = None
        self.height = 1

class AVL:
    def __init__(self):
        self.root = None

    def __repr__(self):

        if self.root == None: return ''
        content = '\n'  # to hold final string
        cur_nodes = [self.root]  # all nodes at current level
        cur_height = self.root.height  # height of nodes at current level
        sep = ' ' * (2 ** (cur_height - 1))  # variable sized separator between elements

        while True:
            cur_height -= 1  # decrement current height
            if len(cur_nodes) == 0: break
            cur_row = ' '
            next_row = ''
            next_nodes = []
            if all(n is None for n in cur_nodes):
                break
            for n in cur_nodes:
                if n == None:
                    cur_row += '   ' + sep
                    next_row += '   ' + sep
                    next_nodes.extend([None, None])
                    continue
                if n.val != None:
                    buf = ' ' * int((5-len(str(n.val))) / 2)
                    cur_row += '%s%s%s' % (buf, str(n.val), buf) + sep
                else:
                    cur_row += ' ' * 5 + sep

                if n.left!= None:
                    next_nodes.append(n.left)
                    next_row += ' /' + sep
                else:
                    next_row += '  ' + sep
                    next_nodes.append(None)

                if n.right!= None:
                    next_nodes.append(n.right)
                    next_row += '\ ' + sep
                else:
                    next_row += '  ' + sep
                    next_nodes.append(None)

            content += (cur_height * '   ' + cur_row + '\n' + cur_height * '   ' + next_row + '\n')
            cur_nodes = next_nodes
            sep = ' ' * int(len(sep) / 2)  # cut separator size in half
        return content

    def insert(self,value):
        #if root is not present then add the root.
        if self.root == None:
            self.root = Node(value)
        else: #visit the insert function
            self._insert(value,self.root)

    def _insert(self,value,cur_node):

        if value < cur_node.val : #cur_node will be self.root in first
            if(cur_node.left==None): #if no left node then add node there
                cur_node.left = Node(value)
                cur_node.left.parent = cur_node
                self.checkInsertion(cur_node.left)
            else: #call left recursively
                return self._insert(value,cur_node.left)
        #doing the same thing with right side
        else:
            if(cur_node.right==None):
                cur_node.right = Node(value)
                cur_node.right.parent = cur_node
                self.checkInsertion(cur_node.right)
            else:
                return self._insert(value,cur_node.right)

    def checkInsertion(self, cur_node, path =[]):

        if cur_node.parent == None:
            return
        path = [cur_node]+path #updating the nodes in the form of list
        left = self.getHeight(cur_node.parent.left)
        right = self.getHeight(cur_node.parent.right)

        if abs(left-right) > 1: #imbalance
            path = [cur_node.parent] + path
            self.rebalancenode(path[0],path[1],path[2])
            return
        new_height = 1+cur_node.height #after balancing the height of node
        if new_height>cur_node.parent.height:
            cur_node.parent.height = new_height

        self.checkInsertion(cur_node.parent,path)

    def rebalancenode(self,z,y,x):

        if y == z.left and x == y.left: #case1: left-left
            self.rightRotate(z)
        elif y ==z.right and x ==y.right: #case2: right-right
            self.leftRotate(z)
        elif y == z.left and x == y.right: #case3 : left-right
            self.leftRotate(y)
            self.rightRotate(z)
        elif y == z.right and x == y.left: #case4 : right-left
            self.rightRotate(y)
            self.leftRotate(z)
        else:
            raise Exception ('Poor METHOD')

    def rightRotate(self,z):
        #saved the changes
        parent = z.parent
        y = z.left
        t3 = y.right
        #making changes
        y.right = z
        z.parent = y
        z.left = t3

        if t3!=None:
            t3.parent = z

        y.parent = parent

        if y.parent == None: #if z was the root node
            self.root = y

        else:
            #if z was the left child
            if y.parent.left ==z:
                y.parent.left = y
            else:#z was the right child
                y.parent.right = y
        z.height = 1 + max(self.getHeight(z.left),self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

    def leftRotate(self,z):
        # saved the changes
        parent = z.parent
        y = z.right
        t3 = y.left
        # making changes
        y.left = z
        z.right = t3
        z.parent = y

        if t3 != None:
            t3.parent = z

        y.parent = parent

        if y.parent == None:  # if z was the root node
            self.root = y

        else:
            # if z was the left child
            if y.parent.left == z:
                y.parent.left = y
            else:  # z was the right child
                y.parent.right = y
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

    def getHeight(self,cur_node):
        if cur_node == None:
            return 0
        else:
            return cur_node.height

    def Inorder(self): #left-> root -> Right
        if self.root != None:
            print("InOrder Taversal :")
            return  self._Inorder(self.root)
        else:
            print("TREE IS EMPTY")
            return

    def _Inorder(self,cur_node):

        if cur_node!=None:
            self._Inorder(cur_node.left)
            print(cur_node.val , end = " ")
            self._Inorder(cur_node.right)

    def Preorder(self): #LEFT-RIGHT-Root
        if self.root != None:
            print("\nPreOrder Taversal :")
            return  self._Preorder(self.root)
        else:
            print("TREE IS EMPTY")
            return

    def _Preorder(self,cur_node):

        if cur_node!=None:
            print(cur_node.val, end=" ")
            self._Preorder(cur_node.left)
            self._Preorder(cur_node.right)

    def Postorder(self): #left -> right-> root
        if self.root != None:
            print("\nPost Order Taversal :")
            return  self._Postorder(self.root)
        else:
            print("TREE IS EMPTY")
            return

    def _Postorder(self,cur_node):

        if cur_node!=None:
            self._Postorder(cur_node.left)
            self._Postorder(cur_node.right)
            print(cur_node.val, end=" ")

    def search(self,value):

        if self.root != None:
            return self._search(self.root , value)
        else:
            return None

    def _search(self,cur_node,value):

        if cur_node.val == value:
            return f"\nSearch for {value}-->Found"

        if value < cur_node.val and cur_node.left!=None:
            return self._search(cur_node.left , value)

        if value >= cur_node.val and cur_node.right!=None:
            return self._search(cur_node.right , value)
        return f"\nSearch for {value}-->Not Found"

    def find(self,value): #Useful in Delete function

        if self.root != None:
            return self._find(self.root , value)
        else:
            return self.root

    def _find(self,cur_node,value):

        if cur_node.val == value:
            return cur_node

        if value < cur_node.val and cur_node.left!=None:
            return self._find(cur_node.left , value)

        if value >= cur_node.val and cur_node.right!=None:
            return self._find(cur_node.right , value)
        return None

    def height(self):
        return self.root.height

    def minval(self):

        if self.root != None:
            return self._minval(self.root)
        else:
            return None

    def _minval(self,cur_node):

        if cur_node.left == None:
            return f"Minimum value Node-->{cur_node.val}"
        else:
            return self._minval(cur_node.left)

    def maxval(self):

        if self.root != None:
            return self._maxval(self.root)
        else:
            return None

    def _maxval(self,cur_node):

        if cur_node.right == None:
            return f"Minimum value Node-->{cur_node.val}"
        else:
            return self._maxval(cur_node.right)

    def sum(self):
        if self.root !=None:
            return f"Sum -->{self._sum(self.root)}"
        else:
            return 0

    def _sum(self,cur_Node):
        if cur_Node == None:
            return 0
        val = cur_Node.val
        if cur_Node.left: #we didn't return the function here so it can add seperately w.r.t to the root node.
            val += self._sum(cur_Node.left)
        if cur_Node.right:
            val += self._sum(cur_Node.right)
        return val

    def delete(self,value):
        return self._delete(self.find(value))

    def _delete(self,cur_node):
        if cur_node == None or self.find(cur_node.val) == None:
            print(f"Node-->{cur_node.val}not in the tree.")
            return
        def minnode(n): #finding the sucessor of the node to be deleted
            current = n
            while current.left!=None:
                current = current.left
            return current
        def numchildren(node): #getting the children for deciding which case it is
            n = 0
            if node.left !=None:
                n += 1
            if node.right !=None:
                n += 1
            return n
        parent = cur_node.parent #saving the parent of the node to be deleted to update it
        childrent_of_node = numchildren(cur_node)

        if childrent_of_node == 0 : #Case 1 i.e no child case.
            if parent !=None:
                if parent.right == cur_node:
                  parent.right = None #if the node to be deleted is right child
                if parent.left == cur_node:
                  parent.left = None #is it is the left child of the node.
            else: #if the deleted root has no parent then it the root node and it has no child
                self.root = None

        if childrent_of_node == 1:
            if parent.left: #left is the child here
                child = cur_node.left
            else:
                child = cur_node.right #else right is the child.

            if parent!=None: #if the cur_node is not the root node then.
                if parent.left == cur_node: #if left child is to be deleted
                    parent.left = child
                else: #if right child is to be deleted
                    parent.right = child
            else: #if it was the root node
                self.root = child

            child.parent = parent#updating the parent of the child

        if childrent_of_node == 2: #case3: when it has 2 children
            suc = minnode(cur_node.right) # the smallest value just above the cur node.
            #get the successor of the node to be deleted
            cur_node.val = suc.val #replace the value of cur node with succ
            #now delete the suc
            self._delete(suc)
            return
        if parent !=None:
            parent.height = 1+max(self.getHeight(parent.left),self.getHeight(parent.right))
            self.checkDelete(parent)

    def checkDelete(self,cur_node):

        if cur_node.parent == None:
            return
        left = self.getHeight(cur_node.parent.left)
        right = self.getHeight(cur_node.parent.right)

        if abs(left-right)>1:
            #if imbalanced then

            y = self.taller_child(cur_node)
            x = self.taller_child(y)
            self.rebalancenode(cur_node,y,x)

        self.checkDelete(cur_node.parent) #checking for all the above parents

    def taller_child(self,cur_node):
        if cur_node == None:
            return 0
        left = self.getHeight(cur_node.parent.left)
        right = self.getHeight(cur_node.parent.right)
        if left>=right:
            return cur_node.left
        else:
            return cur_node.right

    def getroot(self):
        return self.root

tree = AVL()
A = [2, 1, 31, 3, 12, 23,89,90,91,1010,901]

for i in A:
    tree.insert(i)
tree.Inorder()
tree.Preorder()
tree.Postorder()
print('')
print(tree.search(12))
root = tree.getroot()
print(f"ROOT -->{root.val}")
print(f"Height-->{tree.getHeight(root)}")
print(tree.minval())
print(tree.maxval())
print(tree.sum())
print(tree.search(12))
tree.delete(12)
print(tree.__repr__())
print(tree.height())