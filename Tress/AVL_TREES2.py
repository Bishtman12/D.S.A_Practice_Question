class Node:

    def __init__(self, val):
        self.parent = None
        self.left = None
        self.right = None
        self.val = val
        self.height = 1


class AVL:

    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, cur_node, value):
        if value < cur_node.val:
            if cur_node.left:
                return self._insert(cur_node.left,value)
            else:
                cur_node.left = Node(value)
                cur_node.left.parent = cur_node
                self.checkinsert(cur_node.left)
        else:
            if cur_node.right:
                return self._insert(cur_node.right,value)
            else:
                cur_node.right = Node(value)
                cur_node.right.parent = cur_node
                self.checkinsert(cur_node.right)

    def checkinsert(self, cur_node, path=[]):

        if cur_node.parent is None:
            return

        path = [cur_node] + path
        left = self.getheight(cur_node.parent.left)
        right = self.getheight(cur_node.parent.right)
        balance = abs(left - right)

        if balance > 1:
            path = [cur_node.parent] + path
            self.rebalance(path[0], path[1], path[2])
            return
        new_height = 1 + cur_node.height

        if cur_node.parent.height < new_height:
            cur_node.parent.height = new_height
        self.checkinsert(cur_node.parent, path)

    def rebalance(self, z, y, x):

        if y == z.left and x == y.left:  # left left left Case
            self.rightrotate(z)
        elif y == z.right and x == y.right:
            self.leftrotate(z)

        elif y == z.left and x == y.right:
            self.leftrotate(y)
            self.rightrotate(z)
        elif y == z.right and x == y.left:
            self.rightrotate(y)
            self.leftrotate(z)
        else:
            raise Exception("Error")

    def getheight(self, root):

        if not root:
            return 0
        else:
            return root.height

    def rightrotate(self, z):
        #step 1 : Store the 3 variables
        parent = z.parent
        y = z.left
        t3 = y.right
        #Step 2 : Make changes

        y.right = z
        z.left = t3
        z.parent = y
        #Asssign Parents

        if t3 is not None:
            t3.parent = z
        y.parent = parent
        if y.parent is None:
            self.root = y
        else:
            if z == y.parent.left:
                y.parent.left = y
            else:
                y.parent.right = y

        #Update Heights
        y.height = 1 + max(self.getheight(y.left),self.getheight(y.right))
        z.height = 1 + max(self.getheight(z.left),self.getheight(z.right))

    def leftrotate(self, z):
        # Step 1 storing
        parent = z.parent
        y = z.right
        t3 = y.left
        #Step 2 Making Changes

        y.left = z
        z.right = t3
        z.parent = y

        if t3 is not None:
            t3.parent = z

        y.parent = parent

        if y.parent is None:
            self.root =y
        else:
            if y.parent.left == z :
                y.parent.left = y
            else:
                y.parent.right = y

        #first you have to modify the height of z then the height of y because z is the child of y.
        z.height = 1 + max(self.getheight(z.left), self.getheight(z.right))
        y.height = 1 + max(self.getheight(y.left),self.getheight(y.right))


    def height(self):
        if self.root is None:
            return 0

        return self.root.height

    def inorder(self):
        if self.root is None:
            return None
        else:
            return self._inorder(self.root)

    def _inorder(self, cur_node):  # Iterative method
        ans = []
        temp = []
        while True:
            if cur_node:
                temp.append(cur_node)
                cur_node = cur_node.left
            elif temp:
                top = temp.pop()
                ans.append(top.val)
                cur_node = top.right
            else:
                break
        return f"InOrder Traversal -->{ans}"

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
                    buf = ' ' * int((5 - len(str(n.val))) / 2)
                    cur_row += '%s%s%s' % (buf, str(n.val), buf) + sep
                else:
                    cur_row += ' ' * 5 + sep

                if n.left != None:
                    next_nodes.append(n.left)
                    next_row += ' /' + sep
                else:
                    next_row += '  ' + sep
                    next_nodes.append(None)

                if n.right != None:
                    next_nodes.append(n.right)
                    next_row += '\ ' + sep
                else:
                    next_row += '  ' + sep
                    next_nodes.append(None)

            content += (cur_height * '   ' + cur_row + '\n' + cur_height * '   ' + next_row + '\n')
            cur_nodes = next_nodes
            sep = ' ' * int(len(sep) / 2)  # cut separator size in half
        return content

    def getroot(self):
        return self.root.val
    def find(self,node,value):
        if node.val == value:
            return node
        if value < node.val:
            if node.left:
                return self.find(node.left,value)
            else:
                return False
        else:
            if node.right:
                return self.find(node.right,value)
            else:
                return False

    def delete(self,value):

        if self.root is None:
            print("Tree is Empty")
            return
        else:
            node = self.find(self.root,value)
            self._delete(node,value) # returns the node to be deleted

    def _delete(self,cur_node,value): # gets the node to be deleted as the cur_node

        parent = cur_node.parent
        if cur_node.left and cur_node.right : #two child's case (succ then copy and del it)
            pred = self.getmin(cur_node.right)

            cur_node.val = pred.val #storing the pred node
            return self._delete(pred,value) #recalling to delete this node as this will be zero or one child case now
        else:
            child = cur_node.left or cur_node.right
            if cur_node.left : #left child is present copy the left child into the node then delete the left child
                cur_node.val = child.val
                cur_node.left = None
            if cur_node.right :
                cur_node.val = child.val
                cur_node.right = None
            else: #when both child are not present
                if cur_node.parent is None: #root node case
                    self.root = None
                else:
                    if cur_node == cur_node.parent.left:
                        cur_node.parent.left = None
                    else:
                        cur_node.parent.right = None
        self.checkdelete(parent,value)

    def tallerchild(self,node):
        if node is None:
            return None
        left = self.getheight(node.left)
        right = self.getheight(node.right)
        if left>right:
            return node.left
        else:
            return node.right

    def checkdelete(self,cur_node,value):

        if cur_node is None:
            return
        if cur_node.parent is None:
            return
        left = self.getheight(cur_node.left)
        right = self.getheight(cur_node.right)
        balance = abs(left-right)

        if balance > 1:
            y = self.tallerchild(cur_node)
            x = self.tallerchild(y)
            self.rebalance(cur_node,y,x)
        self.checkdelete(cur_node.parent,value)

    def minval(self):
        min = self.getmin(self.root)
        return f"Minimum Value -->{min.val}"

    def getmin(self,node):
        if node.left is None:
            return node
        else:
            return self.getmin(node.left)
myTree = AVL()
A = [2, 1, 31, 3, 12, 23]
for i in A:
    myTree.insert(i)
print(f"Height of the Tree -->{myTree.height()}")
print(myTree.inorder())
print(myTree.__repr__())
print(myTree.getroot())
print(myTree.minval())
myTree.delete(1)
myTree.delete(2)
myTree.delete(23)

print("########AFTER DELETE#######")

print(myTree.inorder())
print(myTree.__repr__())
print(f"Height of the Tree --> {myTree.height()}")