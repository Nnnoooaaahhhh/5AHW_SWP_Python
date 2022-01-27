class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, new_node):
        if self.head:
            last_node = self.head
            while last_node.next != None:
                last_node = last_node.next
            last_node.next = new_node
        else:
            self.head = new_node

    def printList(self):
        tempNode = self.head
        while tempNode != None:
            print(tempNode.data, end=" ")
            tempNode = tempNode.next

    def length(self, linkedList):
        tempNode = linkedList.head
        len = 0
        while tempNode != None:
            len += 1
            tempNode = tempNode.next
        return len


    def sum(self, linkedList):
        sum = 0
        tempNode = linkedList.head
        while tempNode != None:
            sum += tempNode.data
            tempNode = tempNode.next
        return sum

    def avg(self, linkedList):
        return self.sum(linkedList)/self.length(linkedList)

    def max(self, linkedList):
        tempNode = linkedList.head
        max = tempNode.data
        while tempNode != None:
            if tempNode.data > max:
                max = tempNode.data
            tempNode = tempNode.next
        return max

    def min(self, linkedList):
        tempNode = linkedList.head
        min = tempNode.data
        while tempNode != None:
            if tempNode.data < min:
                min = tempNode.data
            tempNode = tempNode.next
        return min

