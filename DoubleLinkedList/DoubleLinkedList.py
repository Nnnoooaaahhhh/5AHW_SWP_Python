import Node as Node

class DoubleLinkedList:
    def __init__(self):
        self.head = None


    def printList(self):
        Node = self.head
        while Node:
            print(Node.data, end=" ")
            Node = Node.next
        print("\n")


    def append(self, newNodeData):
            newNode = Node.Node(newNodeData)
            newNode.next = None
            if self.head is None:
                newNode.head = None
                self.head = newNode
                return
            lastNode = self.head
            while lastNode.next:
                lastNode = lastNode.next
            lastNode.next = newNode
            newNode.prev = lastNode


    def insertAfter(self, node, newNodeData):
        if node is None:
            print("Error, prevNode is None")
            return
        if node > self.length():
            print("Error, index too big")
            return
        if node < 1:
            print("Error, index must be > 0")
            return
        prevNode = self.head
        for i in range(node - 1):
            prevNode = prevNode.next
        newNode = Node.Node(newNodeData)
        newNode.next = prevNode.next
        prevNode.next = newNode
        newNode.prev = prevNode
        if newNode.next:
            newNode.next.prev = newNode


    def insertBefore(self, node, newNodeData):
        if node is None:
            print("Error, prevNode is None")
            return
        if node < 2:
            print("Error, index must be > 1")
            return
        if node > self.length():
            print("Error, index too big")
            return
        befNode = self.head
        for i in range(node - 1):
            befNode = befNode.next
        newNode = Node.Node(newNodeData)
        newNode.prev = befNode.prev
        befNode.prev = newNode
        newNode.next = befNode
        if newNode.prev:
            newNode.prev.next = newNode

    def deleteAfter(self, node):
        if node is None:
            print("Error, prevNode is None")
            return
        if node > self.length():
            print("Error, index too big")
            return
        if node < 1:
            print("Error, index must be > 0")
            return
        prevNode = self.head
        for i in range(node-1):
            prevNode = prevNode.next
        deleteNode = prevNode.next
        afterNode = deleteNode.next
        prevNode.next = deleteNode.next
        afterNode.prev = deleteNode.prev


    def deleteBefore(self, node):
        if node is None:
            print("Error, prevNode is None")
            return
        if node < 2:
            print("Error, index must be > 1")
            return
        if node > self.length():
            print("Error, index too big")
            return
        befNode = self.head
        for i in range(node - 1):
            befNode = befNode.next
        deleteNode = befNode.prev
        afterNode = deleteNode.prev
        befNode.prev = deleteNode.prev
        afterNode.next = deleteNode.next


    def find(self, NodeToFind):
        Node = self.head
        index = 0
        while Node:
            if(Node.data == NodeToFind.data):
                print("found at index " + str(index))
                return
            index += 1
            last = Node
            Node = Node.next
        print("not found")


    def length(self):
        tempNode = self.head
        len = 0
        while tempNode != None:
            len += 1
            tempNode = tempNode.next
        return len
#

    def max(self):
        tempNode = self.head
        max = tempNode.data
        while tempNode != None:
            if tempNode.data > max:
                max = tempNode.data
            tempNode = tempNode.next
        return max


    def min(self):
        tempNode = self.head
        min = tempNode.data
        while tempNode != None:
            if tempNode.data < min:
                min = tempNode.data
            tempNode = tempNode.next
        return min



