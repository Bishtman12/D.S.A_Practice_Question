import sys
class Heap:
    def __init__(self,maxsize):
        self.maxsize = maxsize #maximum size of the binary heap
        self.size = 0 # index of the array
        self.Heap = [0]*(self.maxsize+1) #making a array to store the Binary Heap
        self.Heap[0] = -1*(sys.maxsize) # sotring -inf at the zero index
        self.root = 1 # return the root node of the heap

    def parent(self,i): # is is the index in the array whose parent is to be found
        return i//2
    def leftchild(self,i):
        return 2*i
    def rightchild(self,i):
        return 2*i + 1

    def isLeaf(self,i): # when there is no left(2i) or right(2i+1) child are present in the array.
        if (2*i + 1) >=self.maxsize :
            return False
        return True

    def swap(self,first,second):
        self.Heap[first], self.Heap[second] = self.Heap[second], self.Heap[first]

    def heapify(self,i):
        if not self.isLeaf(i):
            if self.Heap[i] > self.Heap[self.leftchild(i)] or self.Heap[i] > self.Heap[self.rightchild(i)]: # Voilate the heap property
                if self.Heap[self.leftchild(i)] < self.Heap[self.rightchild(i)]: # left child is smaller of the two then swap with the left child
                    self.swap(i,self.leftchild(i))
                    self.heapify(self.leftchild(i)) # the swapped node will be the left child now
                else:
                    self.swap(i,self.rightchild(i))
                    self.heapify(self.rightchild(i))

    def insert(self,value):
        if self.size >= self.maxsize:
            return "FULL"
        # insert the element
        self.size += 1
        self.Heap[self.size] = value
        # place it at the correct position
        cur = self.size
        # keep swaping the nodes till it doesn't voilates the Heap property
        while self.Heap[cur] < self.Heap[self.parent(cur)] :
            self.swap(cur,self.parent(cur))
            cur = self.parent(cur)

    def min(self):
        return self.Heap[self.root]

    def remove(self,): # return the minimum element of the heap then deletes it

        pop = self.Heap[self.root]
        self.Heap[self.root] = self.Heap[self.size] # swapping with the last element of the heap
        self.size -= 1
        self.heapify(self.root)
        return "Deleted"

    def printasarray(self):
        return self.Heap

    def Print(self):
        for i in range(1, (self.size // 2) + 1):
            print(" PARENT : " + str(self.Heap[i]) + " LEFT CHILD : " +
                  str(self.Heap[2 * i]) + " RIGHT CHILD : " +
                  str(self.Heap[2 * i + 1]))

    def klargest(self,k):
        i = 1
        while i< self.maxsize-(k):
            i+=1
        return f"{k} Largest Element-->{self.Heap[i]}"

    def ksmallest(self,k):
        i = 1
        while i< k:
            i+=1
        return f"{k} Smallest Element-->{self.Heap[i]}"
A =  [7 ,10, 4, 3, 20, 15]
n = len(A)+1
heap = Heap(n)
for i in A:
    heap.insert(i)
print(heap.printasarray())
heap.Print()
print(heap.klargest(3))
print(heap.ksmallest(2))


