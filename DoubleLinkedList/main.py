import DoubleLinkedList as dll
import random

if __name__ == "__main__":
    print("main")
    doubleLinkedList = dll.DoubleLinkedList()
    for i in range(50):
        doubleLinkedList.append(random.randint(0, 100))
    """doubleLinkedList.append(1)
    doubleLinkedList.append(2)
    doubleLinkedList.append(6)
    doubleLinkedList.append(5)
    doubleLinkedList.append(2)"""
    """doubleLinkedList.append(3)
    doubleLinkedList.append(2)
    doubleLinkedList.append(1)"""
    doubleLinkedList.printList()
    #doubleLinkedList.insertBeforeNode(doubleLinkedList.head, 9)
    #doubleLinkedList.insertAfterNode(doubleLinkedList.head.next.next.next, 1)
    #doubleLinkedList.insertAfterIndex(1, 323)
    #doubleLinkedList.insertBeforeIndex(45, 384)
    #doubleLinkedList.deleteAfterNode(doubleLinkedList.head.next)
    #doubleLinkedList.deleteBeforeNode(doubleLinkedList.head.next)
    #doubleLinkedList.find(Node.Node(45))
    doubleLinkedList.insSortAsc()
    doubleLinkedList.printList()
    doubleLinkedList.insSortDesc()
    #doubleLinkedList.printList()
    #doubleLinkedList.insSortDesc()
    #print(doubleLinkedList.getNode(0).data)
    #print(doubleLinkedList.length())
    doubleLinkedList.printList()
