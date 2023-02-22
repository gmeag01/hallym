class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
    
class List:
    def __init__(self, data=None):
        self.root = Node(data)
        self.length = 0

    def add(self, data):
        node = self.root
        i = 0
        while node.next != None:
            node = node.next
            i += 1

        node.next = Node(data)
        self.length = i+1
        
    def remove(self, idx):
        if idx > self.length-1 : print('out of index')

        node = self.root
        i = 0
        while i == idx-1:
            node = node.next 
            i += 1

        if node.next.next == None:
            node.next = None

        else:
            node.next = node.next.next

        self.length -= 1

class Stack:
    def __init__(self, data=None):
        self.root = Node(data)

    def push(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            n = Node(data)
            n.next = self.root.next
            self.root.next = n
    
    def pop(self):
        if self.root.next.next == None:
            self.root.next = None
        else:
            n = self.root.next
            self.root.next = self.root.next.next
            n.next = None

class Queue(List):
    def __init__(self, data=None):
        super().__init__(data)

    def remove(self):
        node = self.root
        while node.next.next != None:
            node = node.next

        node.next = None
    




        





            
        


