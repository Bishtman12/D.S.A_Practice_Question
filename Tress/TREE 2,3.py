class Node:
    
    def __init__(self,data, par = None):
    
        self.data = list([data]) #storing the data inside array
        self.parent = par
        self.child = list()

    def printString(self):

        if self.parent:
            return f"{str(self.parent.data)}:{str(self.data)}"
        return f"Root:{str(self.data)}"

    def __lt__(self, node): #checking the sorting order
        return self.data[0] < node.data[0]

    def _isLeaf(self):
        #checking if it has no child
        return len(self.child) == 0

    def _add(self,new_node):




