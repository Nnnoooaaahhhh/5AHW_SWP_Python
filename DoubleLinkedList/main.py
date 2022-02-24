import DoubleLinkedList as dll
import random
import Node

if __name__ == "__main__":
    print("main")
    doubleLinkedList = dll.DoubleLinkedList()
    for i in range(100):
        doubleLinkedList.append(random.randint(0, 100))
    print(doubleLinkedList.length())
    #doubleLinkedList.insertAfter(6, 323)
    #doubleLinkedList.insertBefore(6, 334)
    #doubleLinkedList.deleteAfter(5)
    #doubleLinkedList.deleteBefore(7)
    #doubleLinkedList.find(Node.Node(45))
    print(doubleLinkedList.length())
    doubleLinkedList.printList()
