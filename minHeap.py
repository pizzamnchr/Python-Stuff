import time

class MinHeap:
    # Initializer for the min heap
    def __init__(self):
        self.minHeapList = ["The Min Heap:"]

        self.minHeapSize = 0

    # Function to insert an element into the min heap
    def insert(self, a):
        # Adding the element to the min heap
        self.minHeapList.append(a)
        # Adjusting the size of the min heap
        self.minHeapSize += 1
        # Heapifying the new element into its correct position in the min heap
        self.heapifyUp(self.minHeapSize)

    def extractMin(self):
        if len(self.minHeapList) == 1:
            return 'Empty heap'

        # Getting the root of the min heap
        root = self.minHeapList[1]

        # Replacing the root of the min heap with its last element
        self.minHeapList[1] = self.minHeapList[self.minHeapSize]

        # Getting rid of the min heap's last element since there's a copy in the root
        *self.minHeapList, _ = self.minHeapList

        # Adjusting the size of the min heap
        self.minHeapSize -= 1

        # Heapifying the new root into its correct position in the min heap
        self.heapifyDown(1)

        return root

    # Function to traverse the min heap
    def traverseHeap(self):
        for i in self.minHeapList:
            print(i, end = ' ')

    # Function to move a new element up into its correct position in the min heap
    def heapifyUp(self, b):
        # While the element isn't the root/left element
        while b // 2 > 0:
            # Swap if the element is less than its parent
            if self.minHeapList[b] < self.minHeapList[b // 2]:
                self.minHeapList[b], self.minHeapList[b // 2] = self.minHeapList[b // 2], self.minHeapList[b]

            b = b // 2

    # Function to move a new element down into its correct position in the min heap
    def heapifyDown(self, c):
        while (c * 2) <= self.minHeapSize:
            # Getting the index of the minimum child
            mc = self.minimumChild(c)
            # Swap if the element is greater than its minimum child
            if self.minHeapList[c] > self.minHeapList[mc]:
                self.minHeapList[c], self.minHeapList[mc] = self.minHeapList[mc], self.minHeapList[c]

            c = mc

    # Function to find a node's minimum child
    def minimumChild(self, d):
        # 1 child -> return that child
        if (d * 2) + 1 > self.minHeapSize:
            return d * 2
        else:
            # 2 children -> return the minimum child
            if self.minHeapList[d * 2] < self.minHeapList[(d * 2) + 1]:
                return d * 2
            else:
                return (d * 2) + 1


def main():
    ### SMALL ASCENDING ###

    # Opening file
    textfile = open("smallAscending.txt", "r")
    numbers = textfile.readlines()

    # Starting timer for an empty min heap + insertion of all numbers
    start = time.perf_counter_ns()
    myHeap = MinHeap()

    for element in numbers:
        myHeap.insert(int(element))

    # Stopping timer after all insertions
    stop = time.perf_counter_ns()
    print(f"Time taken for insertion of smallAscending is {stop - start}ns")
    textfile.close()

    # Starting timer for traversal of min heap
    start = time.perf_counter_ns()
    myHeap.traverseHeap()

    # Stopping timer after all numbers are printed
    stop = time.perf_counter_ns()
    print("\n")
    print(f"Time taken for traversal of smallAscending is {stop - start}ns")
    print("\n")

    # Opening file again for deletion of min heap
    textfile = open("smallAscending.txt", "r")
    numbers = textfile.readlines()

    # Starting timer for deletion of min heap
    start = time.perf_counter_ns()

    for element in numbers:
        myHeap.extractMin()

    # Stopping timer after all numbers are deleted
    stop = time.perf_counter_ns()
    print(f"Time taken for deletion of smallAscending is {stop - start}ns")
    print("\n")

    ### MEDIUM ASCENDING ###

    # Opening file
    textfile = open("mediumAscending.txt", "r")
    numbers = textfile.readlines()

    # Starting timer for an empty min heap + insertion of all numbers
    start = time.perf_counter_ns()
    myHeap = MinHeap()

    for element in numbers:
        myHeap.insert(int(element))

    # Stopping timer after all insertions
    stop = time.perf_counter_ns()
    print(f"Time taken for insertion of mediumAscending is {stop - start}ns")
    textfile.close()

    # Starting timer for traversal of min heap
    start = time.perf_counter_ns()
    myHeap.traverseHeap()

    # Stopping timer after all numbers are printed
    stop = time.perf_counter_ns()
    print("\n")
    print(f"Time taken for traversal of mediumAscending is {stop - start}ns")
    print("\n")

    # Opening file again for deletion of min heap
    textfile = open("mediumAscending.txt", "r")
    numbers = textfile.readlines()

    # Starting timer for deletion of min heap
    start = time.perf_counter_ns()

    for element in numbers:
        myHeap.extractMin()

    # Stopping timer after all numbers are deleted
    stop = time.perf_counter_ns()
    print(f"Time taken for deletion of mediumAscending is {stop - start}ns")
    print("\n")

    ### LARGE ASCENDING ###

    # Opening file
    textfile = open("largeAscending.txt", "r")
    numbers = textfile.readlines()

    # Starting timer for an empty min heap + insertion of all numbers
    start = time.perf_counter_ns()
    myHeap = MinHeap()

    for element in numbers:
        myHeap.insert(int(element))

    # Stopping timer after all insertions
    stop = time.perf_counter_ns()
    print(f"Time taken for insertion of largeAscending is {stop - start}ns")
    textfile.close()

    # print("Heap size: " + str(myHeap.minHeapSize))

    # Starting timer for traversal of min heap
    start = time.perf_counter_ns()
    myHeap.traverseHeap()

    # Stopping timer after all numbers are printed
    stop = time.perf_counter_ns()
    print("\n")
    print(f"Time taken for traversal of largeAscending is {stop - start}ns")
    print("\n")

    # Opening file again for deletion of min heap
    textfile = open("largeAscending.txt", "r")
    numbers = textfile.readlines()

    # Starting timer for deletion of min heap
    start = time.perf_counter_ns()

    for element in numbers:
        myHeap.extractMin()

    # Stopping timer after all numbers are deleted
    stop = time.perf_counter_ns()
    print(f"Time taken for deletion of largeAscending is {stop - start}ns")
    print("\n")

    # print("Heap size: " + str(myHeap.minHeapSize))

    ### SMALL DESCENDING ###

    # Opening file
    textfile = open("smallDescending.txt", "r")
    numbers = textfile.readlines()

    # Starting timer for an empty min heap + insertion of all numbers
    start = time.perf_counter_ns()
    myHeap = MinHeap()

    for element in numbers:
        myHeap.insert(int(element))

    # Stopping timer after all insertions
    stop = time.perf_counter_ns()
    print(f"Time taken for insertion of smallDescending is {stop - start}ns")
    textfile.close()

    # Starting timer for traversal of min heap
    start = time.perf_counter_ns()
    myHeap.traverseHeap()

    # Stopping timer after all numbers are printed
    stop = time.perf_counter_ns()
    print("\n")
    print(f"Time taken for traversal of smallDescending is {stop - start}ns")
    print("\n")

    # Opening file again for deletion of min heap
    textfile = open("smallDescending.txt", "r")
    numbers = textfile.readlines()

    # Starting timer for deletion of min heap
    start = time.perf_counter_ns()

    for element in numbers:
        myHeap.extractMin()

    # Stopping timer after all numbers are deleted
    stop = time.perf_counter_ns()
    print(f"Time taken for deletion of smallDescending is {stop - start}ns")
    print("\n")

    ### MEDIUM DESCENDING ###

    # Opening file
    textfile = open("mediumDescending.txt", "r")
    numbers = textfile.readlines()

    # Starting timer for an empty min heap + insertion of all numbers
    start = time.perf_counter_ns()
    myHeap = MinHeap()

    for element in numbers:
        myHeap.insert(int(element))

    # Stopping timer after all insertions
    stop = time.perf_counter_ns()
    print(f"Time taken for insertion of mediumDescending is {stop - start}ns")
    textfile.close()

    # Starting timer for traversal of min heap
    start = time.perf_counter_ns()
    myHeap.traverseHeap()

    # Stopping timer after all numbers are printed
    stop = time.perf_counter_ns()
    print("\n")
    print(f"Time taken for traversal of mediumDescending is {stop - start}ns")
    print("\n")

    # Opening file again for deletion of min heap
    textfile = open("mediumDescending.txt", "r")
    numbers = textfile.readlines()

    # Starting timer for deletion of min heap
    start = time.perf_counter_ns()

    for element in numbers:
        myHeap.extractMin()

    # Stopping timer after all numbers are deleted
    stop = time.perf_counter_ns()
    print(f"Time taken for deletion of mediumDescending is {stop - start}ns")
    print("\n")

    ### LARGE DESCENDING ###

    # Opening file
    textfile = open("largeDescending.txt", "r")
    numbers = textfile.readlines()

    # Starting timer for an empty min heap + insertion of all numbers
    start = time.perf_counter_ns()
    myHeap = MinHeap()

    for element in numbers:
        myHeap.insert(int(element))

    # Stopping timer after all insertions
    stop = time.perf_counter_ns()
    print(f"Time taken for insertion of largeDescending is {stop - start}ns")
    textfile.close()

    # print("Heap size: " + str(myHeap.minHeapSize))

    # Starting timer for traversal of min heap
    start = time.perf_counter_ns()
    myHeap.traverseHeap()

    # Stopping timer after all numbers are printed
    stop = time.perf_counter_ns()
    print("\n")
    print(f"Time taken for traversal of largeDescending is {stop - start}ns")
    print("\n")

    # Opening file again for deletion of min heap
    textfile = open("largeDescending.txt", "r")
    numbers = textfile.readlines()

    # Starting timer for deletion of min heap
    start = time.perf_counter_ns()

    for element in numbers:
        myHeap.extractMin()

    # Stopping timer after all numbers are deleted
    stop = time.perf_counter_ns()
    print(f"Time taken for deletion of largeDescending is {stop - start}ns")
    print("\n")

    # print("Heap size: " + str(myHeap.minHeapSize))

    ### SMALL RANDOM ###

    # Opening file
    textfile = open("smallRandom.txt", "r")
    numbers = textfile.readlines()

    # Starting timer for an empty min heap + insertion of all numbers
    start = time.perf_counter_ns()
    myHeap = MinHeap()

    for element in numbers:
        myHeap.insert(int(element))

    # Stopping timer after all insertions
    stop = time.perf_counter_ns()
    print(f"Time taken for insertion of smallRandom is {stop - start}ns")
    textfile.close()

    # Starting timer for traversal of min heap
    start = time.perf_counter_ns()
    myHeap.traverseHeap()

    # Stopping timer after all numbers are printed
    stop = time.perf_counter_ns()
    print("\n")
    print(f"Time taken for traversal of smallRandom is {stop - start}ns")
    print("\n")

    # Opening file again for deletion of min heap
    textfile = open("smallRandom.txt", "r")
    numbers = textfile.readlines()

    # Starting timer for deletion of min heap
    start = time.perf_counter_ns()

    for element in numbers:
        myHeap.extractMin()

    # Stopping timer after all numbers are deleted
    stop = time.perf_counter_ns()
    print(f"Time taken for deletion of smallRandom is {stop - start}ns")
    print("\n")

    ### MEDIUM RANDOM ###

    # Opening file
    textfile = open("mediumRandom.txt", "r")
    numbers = textfile.readlines()

    # Starting timer for an empty min heap + insertion of all numbers
    start = time.perf_counter_ns()
    myHeap = MinHeap()

    for element in numbers:
        myHeap.insert(int(element))

    # Stopping timer after all insertions
    stop = time.perf_counter_ns()
    print(f"Time taken for insertion of mediumRandom is {stop - start}ns")
    textfile.close()

    # Starting timer for traversal of min heap
    start = time.perf_counter_ns()
    myHeap.traverseHeap()

    # Stopping timer after all numbers are printed
    stop = time.perf_counter_ns()
    print("\n")
    print(f"Time taken for traversal of mediumRandom is {stop - start}ns")
    print("\n")

    # Opening file again for deletion of min heap
    textfile = open("mediumRandom.txt", "r")
    numbers = textfile.readlines()

    # Starting timer for deletion of min heap
    start = time.perf_counter_ns()

    for element in numbers:
        myHeap.extractMin()

    # Stopping timer after all numbers are deleted
    stop = time.perf_counter_ns()
    print(f"Time taken for deletion of mediumRandom is {stop - start}ns")
    print("\n")

    ### LARGE RANDOM ###

    # Opening file
    textfile = open("largeRandom.txt", "r")
    numbers = textfile.readlines()

    # Starting timer for an empty min heap + insertion of all numbers
    start = time.perf_counter_ns()
    myHeap = MinHeap()

    for element in numbers:
        myHeap.insert(int(element))

    # Stopping timer after all insertions
    stop = time.perf_counter_ns()
    print(f"Time taken for insertion of largeRandom is {stop - start}ns")
    textfile.close()

    # print("Heap size: " + str(myHeap.minHeapSize))

    # Starting timer for traversal of min heap
    start = time.perf_counter_ns()
    myHeap.traverseHeap()

    # Stopping timer after all numbers are printed
    stop = time.perf_counter_ns()
    print("\n")
    print(f"Time taken for traversal of largeRandom is {stop - start}ns")
    print("\n")

    # Opening file again for deletion of min heap
    textfile = open("largeRandom.txt", "r")
    numbers = textfile.readlines()

    # Starting timer for deletion of min heap
    start = time.perf_counter_ns()

    for element in numbers:
        myHeap.extractMin()

    # Stopping timer after all numbers are deleted
    stop = time.perf_counter_ns()
    print(f"Time taken for deletion of largeRandom is {stop - start}ns")
    print("\n")

    # print("Heap size: " + str(myHeap.minHeapSize))

main()
