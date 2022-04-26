class Node:
    def __init__(self,data=None):
        self.left = None
        self.right = None
        self.val = data
        self.parent = None
        self.height = 1

class BST:
    def __init__(self):
        self.root = None

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
            else: #call left recursively
                return self._insert(value,cur_node.left)
        #doing the same thing with right side
        else:
            if(cur_node.right==None):
                cur_node.right = Node(value)
                cur_node.right.parent = cur_node
            else:
                return self._insert(value,cur_node.right)

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

        if self.root!=None:
            return self._height(self.root , height=1)
        else:
            return 0

    def _height(self,cur_node,height):

        if cur_node == None:
            return f"Height of Tree-->{height}"
        left = self._height(cur_node.left,height+1)
        right = self._height(cur_node.right , height+1)
        return max(left,right)

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

tree = BST()
A = [2,1,31,3,12,31,23,123]

for i in A:
    tree.insert(i)
tree.Inorder()
tree.Preorder()
tree.Postorder()
print('')
print(tree.search(12))
print(tree.height())
print(tree.minval())
print(tree.maxval())
print(tree.sum())
tree.delete(12)
print(tree.search(12))