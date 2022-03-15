import DoubleLinkedList as dll
import random
import Arraylist as al
import time

if __name__ == "__main__":
    print("main")
    doubleLinkedList = dll.DoubleLinkedList()
    arrayList = al.Arraylist()
    for i in range(10000):
        x = random.randint(0, 10000)
        doubleLinkedList.append(x)
        arrayList.append(x)
    arrayList.printAll()
    print("\n")
    doubleLinkedList.printList()
    start = time.time()
    doubleLinkedList.insSortAsc()
    end = time.time()
    print(end-start)
    start = time.time()
    arrayList.sortAsc()
    end = time.time()
    print(end - start)
    arrayList.printAll()
    print("\n")
    doubleLinkedList.printList()

    #ArrayList Methoden
    #arrayList.append(34)
    #arrayList.append(10)
    #arrayList.append(283)
    #print(arrayList.getMax())
    #print(arrayList.getMin())
    #arrayList.deleteBefore(4)
    #arrayList.deleteAfter(1)
    #print(arrayList.getLength())
    #arrayList.insertBefore(2, 199)
    #arrayList.insertAfter(0, 129)
    #arrayList.sortDesc()
    #arrayList.sortAsc()

    #Double Linked List Methoden
    #doubleLinkedList.insertBeforeNode(doubleLinkedList.head, 9)
    #doubleLinkedList.insertAfterNode(doubleLinkedList.head.next.next.next, 1)
    #doubleLinkedList.insertAfterIndex(1, 323)
    #doubleLinkedList.insertBeforeIndex(45, 384)
    #doubleLinkedList.deleteAfterNode(doubleLinkedList.head.next)
    #doubleLinkedList.deleteBeforeNode(doubleLinkedList.head.next)
    #doubleLinkedList.find(Node.Node(45))
    #doubleLinkedList.insSortAsc()
    #doubleLinkedList.insSortDesc()
    #print(doubleLinkedList.length())
    #print(doubleLinkedList.Max())
    #print(doubleLinkedList.min())
