class Arraylist:
    def __init__(self):
        self.list = []

    def append(self, value):
        self.list.append(value)

    def getLength(self):
        return len(self.list)

    def printAll(self):
        for i in self.list:
            print(str(i), end=" ")

    def getMax(self):
        return max(self.list)

    def getMin(self):
        return min(self.list)

    def deleteBefore(self, index):
        if index is None:
            return
        elif index <= 0:
            print("Can't delete before 0")
            return
        elif index > self.getLength():
            print("Index too big")
            return
        else:
            self.list.pop(index-1)

    def deleteAfter(self, index):
        if index is None:
            return
        elif index < 0:
            print("Can't delete after negativ index")
            return
        elif index > self.getLength()-2:
            print("Index too big")
            return
        else:
            self.list.pop(index+1)

    def insertBefore(self, index, value):
        if index is None:
            return
        elif index < 0:
            print("Can't delete before 0")
            return
        elif index > self.getLength() - 1:
            print("Index too big")
            return
        else:
            self.list.insert(index, value)


    def insertAfter(self, index, value):
        if index is None:
            return
        elif index < 0:
            print("Can't delete after negativ index")
            return
        elif index > self.getLength()-1:
            print("Index too big")
            return
        else:
            self.list.insert(index +  1, value)


    def clear(self):
        self.list.clear()

    def sortAsc(self):
        for i in range(1, self.getLength()):
            key = self.list[i]
            j = i - 1
            while j >= 0 and key < self.list[j]:
                self.list[j + 1] = self.list[j]
                j -= 1
            self.list[j + 1] = key



    def sortDesc(self):
        for i in range(1, self.getLength()):
            key = self.list[i]
            j = i-1
            while j>= 0 and key > self.list[j]:
                self.list[j+1] = self.list[j]
                j -= 1
            self.list[j+1] = key
