from collections import deque
import time
import sys
sys.setrecursionlimit(20000)

class Node:
    # Constructor for BST node
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

    # Function for inserting node into BST
    def insert(self, data):
        if self.value == data:
            return False
        # If less, go left
        elif self.value > data:
            if self.left:
                return self.left.insert(data)
            else:
                self.left = Node(data)
                return True
        # Else, go right
        else:
            if self.right:
                return self.right.insert(data)
            else:
                self.right = Node(data)
                return True

    # Function to level order traverse through the BST
    def levelOrderTraversal(self):
        if not self:
            return
 
        # Using a queue to level order traverse the BST
        queue = deque()

        # Putting the current node into the queue
        queue.append(self)
 
        # While the queue isn't empty, put the nodes on each level into the queue
        while queue:
            currentNode = queue.popleft()
 
            print(currentNode.value, end=' ')
 
            if currentNode.left:
                queue.append(currentNode.left)
 
            if currentNode.right:
                queue.append(currentNode.right)

class Tree:
    # Constructor for the BST
    def __init__(self):
        self.root = None

    # Function for inserting into the BST
    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    # Function to level order traverse through the BST
    def levelOrderTraversal(self):
        if self.root is not None:
            print("BST level order: ")
            self.root.levelOrderTraversal()

    # Function to delete a node from the BST
    def delete(self, data):
        if self.root is None:
            return False
        # For if we have to delete the root node of the tree
        elif self.root.value == data:
            if self.root.left is None and self.root.right is None:
                self.root = None

            elif self.root.left and self.root.right is None:
                self.root = self.root.left

            elif self.root.left is None and self.root.right:
                self.root = self.root.right

            elif self.root.left and self.root.right:
                parentToDelete = self.root
                nodeToDelete = self.root.right

                while nodeToDelete.left:
                    parentToDelete = nodeToDelete
                    nodeToDelete = nodeToDelete.left
                    
                if nodeToDelete.right:
                    if parentToDelete.value > nodeToDelete.value:
                        parentToDelete.left = nodeToDelete.right
                        
                    elif parentToDelete.value < nodeToDelete.value:
                        parentToDelete.right = nodeToDelete.right
                else:
                    if nodeToDelete.value < parentToDelete.value:
                        parentToDelete.left = None
                    else:
                        parentToDelete.right = None
                self.root.value = nodeToDelete.value
                        
            return True
        
        node = self.root

        parentNode = None

        # Searching for the node we have to delete if it's not in the root node
        while node and node.value != data:
            parentNode = node
            if data < node.value:
                node = node.left
            elif data > node.value:
                node = node.right
        
        # Return false if we can't find the node we have to delete
        if node is None or node.value != data:
            return False
            
        # If the node we have to delete has no children
        elif node.left is None and node.right is None:
            if data < parentNode.value:
                parentNode.left = None
            else:
                parentNode.right = None
            return True
            
        # If the node we have to delete only has a left child node
        elif node.left and node.right is None:
            if data < parentNode.value:
                parentNode.left = node.left
            else:
                parentNode.right = node.left
            return True
            
        # If the node we have to delete only has a right child node
        elif node.left is None and node.right:
            if data < parentNode.value:
                parentNode.left = node.right
            else:
                parentNode.right = node.right
            return True
            
        # If the node we have to delete has a left child node and a right child node
        else:
            parentToDelete = node
            nodeToDelete = node.right

            while nodeToDelete.left:
                parentToDelete = nodeToDelete
                nodeToDelete = nodeToDelete.left
                
            node.value = nodeToDelete.value

            if nodeToDelete.right:
                if parentToDelete.value > nodeToDelete.value:
                    parentToDelete.left = nodeToDelete.right

                elif parentToDelete.value < nodeToDelete.value:
                    parentToDelete.right = nodeToDelete.right
            else:
                if nodeToDelete.value < parentToDelete.value:
                    parentToDelete.left = None
                else:
                    parentToDelete.right = None

def main():
    ### SMALL ASCENDING ###

    # Opening file
    textfile = open("smallAscending.txt", "r")
    numbers = textfile.readlines()

    # Starting timer for an empty tree + insertion of all numbers
    start = time.perf_counter_ns()
    bst = Tree()

    for element in numbers:
        bst.insert(int(element))

    # Stopping timer after all insertions
    stop = time.perf_counter_ns()
    print(f"Time taken for insertion of smallAscending is {stop - start}ns")
    textfile.close()

    # Starting timer for traversal of BST
    start = time.perf_counter_ns()
    bst.levelOrderTraversal()

    # Stopping timer after all numbers are printed
    stop = time.perf_counter_ns()
    print("\n")
    print(f"Time taken for traversal of smallAscending is {stop - start}ns")
    print("\n")

    # Opening file again for deletion of BST
    textfile = open("smallAscending.txt", "r")
    numbers = textfile.readlines()

    # Starting timer for deletion of BST
    start = time.perf_counter_ns()

    for element in numbers:
        bst.delete(int(element))

    # Stopping timer after all numbers are deleted
    stop = time.perf_counter_ns()
    print(f"Time taken for deletion of smallAscending is {stop - start}ns")
    print("\n")

    # Should do nothing if empty
    # bst.levelOrderTraversal()

    ### MEDIUM ASCENDING ###

    # Opening file
    textfile = open("mediumAscending.txt", "r")
    numbers = textfile.readlines()

    # Starting timer for an empty tree + insertion of all numbers
    start = time.perf_counter_ns()
    bst = Tree()

    for element in numbers:
        bst.insert(int(element))

    # Stopping timer after all insertions
    stop = time.perf_counter_ns()
    print(f"Time taken for insertion of mediumAscending is {stop - start}ns")
    textfile.close()

    # Starting timer for traversal of BST
    start = time.perf_counter_ns()
    bst.levelOrderTraversal()

    # Stopping timer after all numbers are printed
    stop = time.perf_counter_ns()
    print("\n")
    print(f"Time taken for traversal of mediumAscending is {stop - start}ns")
    print("\n")

    # Opening file again for deletion of BST
    textfile = open("mediumAscending.txt", "r")
    numbers = textfile.readlines()

    # Starting timer for deletion of BST
    start = time.perf_counter_ns()

    for element in numbers:
        bst.delete(int(element))

    # Stopping timer after all numbers are deleted
    stop = time.perf_counter_ns()
    print(f"Time taken for deletion of mediumAscending is {stop - start}ns")
    print("\n")

    # Should do nothing if empty
    # bst.levelOrderTraversal()

    ### LARGE ASCENDING ###

    # Opening file
    textfile = open("largeAscending.txt", "r")
    numbers = textfile.readlines()

    # Starting timer for an empty tree + insertion of all numbers
    start = time.perf_counter_ns()
    bst = Tree()

    for element in numbers:
        bst.insert(int(element))

    # Stopping timer after all insertions
    stop = time.perf_counter_ns()
    print(f"Time taken for insertion of largeAscending is {stop - start}ns")
    textfile.close()

    # Starting timer for traversal of BST
    start = time.perf_counter_ns()
    bst.levelOrderTraversal()

    # Stopping timer after all numbers are printed
    stop = time.perf_counter_ns()
    print("\n")
    print(f"Time taken for traversal of largeAscending is {stop - start}ns")
    print("\n")

    # Opening file again for deletion of BST
    textfile = open("largeAscending.txt", "r")
    numbers = textfile.readlines()

    # Starting timer for deletion of BST
    start = time.perf_counter_ns()

    for element in numbers:
        bst.delete(int(element))

    # Stopping timer after all numbers are deleted
    stop = time.perf_counter_ns()
    print(f"Time taken for deletion of largeAscending is {stop - start}ns")
    print("\n")

    # Should do nothing if empty
    # bst.levelOrderTraversal()

    ### SMALL DESCENDING ###

    # Opening file
    textfile = open("smallDescending.txt", "r")
    numbers = textfile.readlines()

    # Starting timer for an empty tree + insertion of all numbers
    start = time.perf_counter_ns()
    bst = Tree()

    for element in numbers:
        bst.insert(int(element))

    # Stopping timer after all insertions
    stop = time.perf_counter_ns()
    print(f"Time taken for insertion of smallDescending is {stop - start}ns")
    textfile.close()

    # Starting timer for traversal of BST
    start = time.perf_counter_ns()
    bst.levelOrderTraversal()

    # Stopping timer after all numbers are printed
    stop = time.perf_counter_ns()
    print("\n")
    print(f"Time taken for traversal of smallDescending is {stop - start}ns")
    print("\n")

    # Opening file again for deletion of BST
    textfile = open("smallDescending.txt", "r")
    numbers = textfile.readlines()

    # Starting timer for deletion of BST
    start = time.perf_counter_ns()

    for element in numbers:
        bst.delete(int(element))

    # Stopping timer after all numbers are deleted
    stop = time.perf_counter_ns()
    print(f"Time taken for deletion of smallDescending is {stop - start}ns")
    print("\n")

    # Should do nothing if empty
    # bst.levelOrderTraversal()

    ### MEDIUM DESCENDING ###

    # Opening file
    textfile = open("mediumDescending.txt", "r")
    numbers = textfile.readlines()

    # Starting timer for an empty tree + insertion of all numbers
    start = time.perf_counter_ns()
    bst = Tree()

    for element in numbers:
        bst.insert(int(element))

    # Stopping timer after all insertions
    stop = time.perf_counter_ns()
    print(f"Time taken for insertion of mediumDescending is {stop - start}ns")
    textfile.close()

    # Starting timer for traversal of BST
    start = time.perf_counter_ns()
    bst.levelOrderTraversal()

    # Stopping timer after all numbers are printed
    stop = time.perf_counter_ns()
    print("\n")
    print(f"Time taken for traversal of mediumDescending is {stop - start}ns")
    print("\n")

    # Opening file again for deletion of BST
    textfile = open("mediumDescending.txt", "r")
    numbers = textfile.readlines()

    # Starting timer for deletion of BST
    start = time.perf_counter_ns()

    for element in numbers:
        bst.delete(int(element))

    # Stopping timer after all numbers are deleted
    stop = time.perf_counter_ns()
    print(f"Time taken for deletion of mediumDescending is {stop - start}ns")
    print("\n")

    # Should do nothing if empty
    # bst.levelOrderTraversal()

    ### LARGE DESCENDING ###

    # Opening file
    textfile = open("largeDescending.txt", "r")
    numbers = textfile.readlines()

    # Starting timer for an empty tree + insertion of all numbers
    start = time.perf_counter_ns()
    bst = Tree()

    for element in numbers:
        bst.insert(int(element))

    # Stopping timer after all insertions
    stop = time.perf_counter_ns()
    print(f"Time taken for insertion of largeDescending is {stop - start}ns")
    textfile.close()

    # Starting timer for traversal of BST
    start = time.perf_counter_ns()
    bst.levelOrderTraversal()

    # Stopping timer after all numbers are printed
    stop = time.perf_counter_ns()
    print("\n")
    print(f"Time taken for traversal of largeDescending is {stop - start}ns")
    print("\n")

    # Opening file again for deletion of BST
    textfile = open("largeDescending.txt", "r")
    numbers = textfile.readlines()

    # Starting timer for deletion of BST
    start = time.perf_counter_ns()

    for element in numbers:
        bst.delete(int(element))

    # Stopping timer after all numbers are deleted
    stop = time.perf_counter_ns()
    print(f"Time taken for deletion of largeDescending is {stop - start}ns")
    print("\n")

    # Should do nothing if empty
    # bst.levelOrderTraversal()

    ### SMALL RANDOM ###

    # Opening file
    textfile = open("smallRandom.txt", "r")
    numbers = textfile.readlines()

    # Starting timer for an empty tree + insertion of all numbers
    start = time.perf_counter_ns()
    bst = Tree()

    for element in numbers:
        bst.insert(int(element))

    # Stopping timer after all insertions
    stop = time.perf_counter_ns()
    print(f"Time taken for insertion of smallRandom is {stop - start}ns")
    textfile.close()

    # Starting timer for traversal of BST
    start = time.perf_counter_ns()
    bst.levelOrderTraversal()

    # Stopping timer after all numbers are printed
    stop = time.perf_counter_ns()
    print("\n")
    print(f"Time taken for traversal of smallRandom is {stop - start}ns")
    print("\n")

    # Opening file again for deletion of BST
    textfile = open("smallRandom.txt", "r")
    numbers = textfile.readlines()

    # Starting timer for deletion of BST
    start = time.perf_counter_ns()

    for element in numbers:
        bst.delete(int(element))

    # Stopping timer after all numbers are deleted
    stop = time.perf_counter_ns()
    print(f"Time taken for deletion of smallRandom is {stop - start}ns")
    print("\n")

    # Should do nothing if empty
    # bst.levelOrderTraversal()

    ### MEDIUM RANDOM ###

    # Opening file
    textfile = open("mediumRandom.txt", "r")
    numbers = textfile.readlines()

    # Starting timer for an empty tree + insertion of all numbers
    start = time.perf_counter_ns()
    bst = Tree()

    for element in numbers:
        bst.insert(int(element))

    # Stopping timer after all insertions
    stop = time.perf_counter_ns()
    print(f"Time taken for insertion of mediumRandom is {stop - start}ns")
    textfile.close()

    # Starting timer for traversal of BST
    start = time.perf_counter_ns()
    bst.levelOrderTraversal()

    # Stopping timer after all numbers are printed
    stop = time.perf_counter_ns()
    print("\n")
    print(f"Time taken for traversal of mediumRandom is {stop - start}ns")
    print("\n")

    # Opening file again for deletion of BST
    textfile = open("mediumRandom.txt", "r")
    numbers = textfile.readlines()

    # Starting timer for deletion of BST
    start = time.perf_counter_ns()

    for element in numbers:
        bst.delete(int(element))

    # Stopping timer after all numbers are deleted
    stop = time.perf_counter_ns()
    print(f"Time taken for deletion of mediumRandom is {stop - start}ns")
    print("\n")

    # Should do nothing if empty
    # bst.levelOrderTraversal()

    ### LARGE RANDOM ###

    # Opening file
    textfile = open("largeRandom.txt", "r")
    numbers = textfile.readlines()

    # Starting timer for an empty tree + insertion of all numbers
    start = time.perf_counter_ns()
    bst = Tree()

    for element in numbers:
        bst.insert(int(element))

    # Stopping timer after all insertions
    stop = time.perf_counter_ns()
    print(f"Time taken for insertion of largeRandom is {stop - start}ns")
    textfile.close()

    # Starting timer for traversal of BST
    start = time.perf_counter_ns()
    bst.levelOrderTraversal()

    # Stopping timer after all numbers are printed
    stop = time.perf_counter_ns()
    print("\n")
    print(f"Time taken for traversal of largeRandom is {stop - start}ns")
    print("\n")

    # Opening file again for deletion of BST
    textfile = open("largeRandom.txt", "r")
    numbers = textfile.readlines()

    # Starting timer for deletion of BST
    start = time.perf_counter_ns()

    for element in numbers:
        bst.delete(int(element))

    # Stopping timer after all numbers are deleted
    stop = time.perf_counter_ns()
    print(f"Time taken for deletion of largeRandom is {stop - start}ns")
    print("\n")

    # Should do nothing if empty
    # bst.levelOrderTraversal()
    
main()