import Node
import LinkedList
import random


if __name__ == "__main__":
    linkedList = LinkedList.LinkedList()
    for i in range(10):
        linkedList.insert(Node.Node(random.randint(0, 100)))
    linkedList.printList()
    print()
    print(linkedList.sum(linkedList))
    print(linkedList.length(linkedList))
    print(linkedList.avg(linkedList))
    print(linkedList.max(linkedList))
    print(linkedList.min(linkedList))
