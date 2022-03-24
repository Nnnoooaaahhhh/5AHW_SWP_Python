import Node as Node


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

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

    def insertAfterIndex(self, node, newNodeData):
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

    def insertAfterNode(self, prevNode, newNodeData):
        if prevNode is None:
            newNode = Node.Node(newNodeData)
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode
            return
        newNode = Node.Node(newNodeData)
        newNode.next = prevNode.next
        prevNode.next = newNode
        newNode.prev = prevNode
        if newNode.next:
            newNode.next.prev = newNode

    def insertBeforeIndex(self, node, newNodeData):
        if node is None:
            print("Error, prevNode is None")
            return
        if node < 1:
            print("Error, index must be > 0")
            return
        if node > self.length():
            print("Error, index too big")
            return
        befNode = self.head
        newNode = Node.Node(newNodeData)
        for i in range(node - 1):
            befNode = befNode.next
        if befNode is self.head:
            a = self.head
            self.head = newNode
            newNode.next = a
            a.prev = newNode
            newNode.prev = None
            return
        newNode.prev = befNode.prev
        befNode.prev = newNode
        newNode.next = befNode
        if newNode.prev:
            newNode.prev.next = newNode

    def insertBeforeNode(self, befNode, newNodeData):
        newNode = Node.Node(newNodeData)
        if befNode is None:
            print("Node falsch!")
            return
        if befNode is self.head:
            a = self.head
            self.head = newNode
            newNode.next = a
            a.prev = newNode
            newNode.prev = None
            return
        newNode.prev = befNode.prev
        befNode.prev = newNode
        newNode.next = befNode
        if newNode.prev:
            newNode.prev.next = newNode

    def deleteAfterIndex(self, node):
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
        deleteNode = prevNode.next
        afterNode = deleteNode.next
        prevNode.next = deleteNode.next
        afterNode.prev = deleteNode.prev

    def deleteAfterNode(self, prevNode):
        if prevNode.next is None:
            print("Node falsch! (After)")
            return
        prevNode = prevNode
        deleteNode = prevNode.next
        afterNode = None
        if deleteNode.next is not None:
            afterNode = deleteNode.next
        prevNode.next = deleteNode.next
        if afterNode is not None:
            afterNode.prev = deleteNode.prev

    def deleteBeforeIndex(self, node):
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

    def deleteBeforeNode(self, afterNode):
        if afterNode.prev is None:
            print("Node falsch! (Before)")
            return
        afterNode = afterNode
        deleteNode = afterNode.prev
        beforeNode = deleteNode.prev
        beforeNode.next = afterNode
        afterNode.prev = afterNode

    def find(self, NodeToFind):
        Node = self.head
        index = 0
        while Node:
            if Node.data is NodeToFind.data:
                print("found at index " + str(index))
                return
            index += 1
            Node = Node.next
        print("not found")

    def length(self):
        tempNode = self.head
        len = 0
        while tempNode is not None:
            len += 1
            tempNode = tempNode.next
        return len

    def max(self):
        tempNode = self.head
        max = tempNode.data
        while tempNode is not None:
            if tempNode.data > max:
                max = tempNode.data
            tempNode = tempNode.next
        return max

    def min(self):
        tempNode = self.head
        min = tempNode.data
        while tempNode is not None:
            if tempNode.data < min:
                min = tempNode.data
            tempNode = tempNode.next
        return min

    def clear(self):
        while (self.head != None):
            temp = self.head
            self.head = self.head.next
            temp = None


    def insSortAsc(self):
        key = self.head
        while key is not None:
            start = self.head
            while key is not start:
                if key.data < start.data:
                    self.insertAfterNode(start.prev, key.data)
                    self.deleteAfterNode(key.prev)
                    break
                start = start.next
            key = key.next


    def insSortDesc(self):
        key = self.head
        while key is not None:
            start = self.head
            while key is not start:
                if key.data > start.data:
                    self.insertAfterNode(start.prev, key.data)
                    self.deleteAfterNode(key.prev)
                    break
                start = start.next
            key = key.next

    def getNode(self, index):
        tempNode = self.head
        for i in range(index):
            tempNode = tempNode.next
        return tempNode
