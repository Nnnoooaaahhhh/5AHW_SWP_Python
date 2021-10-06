def bubbleSort(list):
    for i in range(len(list)):
        for y in range(len(list) - 1 - i):
            if list[y + 1] < list[y]:
                list[y], list[y + 1] = list[y + 1], list[y]
    return list


def insertionSort(list):
    for i in range(1, len(list)):
        key = list[i]
        y = i - 1
        while y >= 0 and key < list[y]:
            list[y+1] = list[y]
            y -= 1
        list[y+1] = key
    return list


def selectionSort(list):
    for i in range(len(list)):
        minindex = i
        for y in range(i+1, len(list)):
            if list[minindex] > list[y]:
                minindex = y
        list[i], list[minindex] = list[minindex], list[i]
    return list


if __name__ == "__main__":
    mList = [2, 3, 9, 1, 8, 10, 2, 7, 6, 5]

    bubList = bubbleSort(mList)
    print(bubList)

    insList = insertionSort(mList)
    print(insList)

    selList = selectionSort(mList)
    print(selList)
