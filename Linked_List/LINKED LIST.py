class Node():

    def __init__(self,pre=None,data=None,next=None):
        self.pre = pre
        self.data = data
        self.next = next

class Dlist():

    def __init__(self):
        self.head = None

    def addbegin(self,value):
        new = Node(data=value)
        new.next = self.head
        new.pre = None #here pre and next both are none
         #here next is pointing to the previous first element

        if(self.head != None):
            self.head.pre = new

        self.head = new

    def print(self):
        temp = self.head
        while (temp):
            print("%d" % temp.data, end=", ")
            temp = temp.next

    def addlast(self,value):
        new = Node(data = value)
        new.next = None
        temp = self.head
        while (temp.next!=None):
            temp = temp.next
        temp.next = new
        new.pre = temp
    def popbegin(self):
        temp = self.head
        self.head = temp.next
        temp.next.pre = None
    def poplast(self):
        temp = self.head
        while(temp.next!=None):
            temp = temp.next
        temp.pre.next = None




list = Dlist()
list.addbegin(4)
list.addbegin(5)
list.addbegin(6)
list.addbegin(7)
list.addlast(10)
list.poplast()
list.print()
