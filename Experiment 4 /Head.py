MAX = 100

heap = [0] * MAX
heapSize = 0


def insert(value):
    global heapSize

    if heapSize == MAX:
        print("Heap Overflow")
        return

    i = heapSize
    heap[i] = value
    heapSize += 1

    # Heapify up
    while i != 0 and heap[(i - 1) // 2] < heap[i]:
        heap[i], heap[(i - 1) // 2] = heap[(i - 1) // 2], heap[i]
        i = (i - 1) // 2


def heapify(i):
    global heapSize

    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < heapSize and heap[left] > heap[largest]:
        largest = left

    if right < heapSize and heap[right] > heap[largest]:
        largest = right

    if largest != i:
        heap[i], heap[largest] = heap[largest], heap[i]
        heapify(largest)


def deleteRoot():
    global heapSize

    if heapSize <= 0:
        print("Heap Underflow")
        return -1

    root = heap[0]
    heap[0] = heap[heapSize - 1]
    heapSize -= 1

    heapify(0)

    return root


def printHeap():
    for i in range(heapSize):
        print(heap[i], end=" ")
    print()


# Main
if __name__ == "__main__":
    insert(10)
    insert(30)
    insert(20)
    insert(5)
    insert(40)

    print("Heap after insertion:")
    printHeap()

    print("Deleted root:", deleteRoot())

    print("Heap after deletion:")
    printHeap()
