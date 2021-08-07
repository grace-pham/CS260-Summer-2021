# Mark Boady CS260 - Heap Homework

# Finish Implementation of this Heap
import math


class Heap:
    # Constructor - Do Not Change
    def __init__(self, capacity):
        # How big the Array is
        self.max_size = capacity
        # How many elements in it
        self.current_size = 0
        # The array itself
        self.data = [None] * self.max_size

    # String Method - Do Not Change
    def __str__(self):
        res = ""
        res += "Heap Current Size: %d\n" % (self.current_size)
        res += "Heap Max Size: %d\n" % (self.max_size)
        res += "Contents:\n"
        for i in range(0, self.current_size):
            res += "H[%d]=%d\n" % (i, self.data[i])
        res += "\n"
        return res

    # You may Change the Implementation of any function below this line.
    # You may NOT change the signature (input arguments/return value)

    # Is the list empty? True/False
    def empty(self):
        if self.current_size == 0:
            return True
        else:
            return False

    # What is the min value? Return None if empty
    def min(self):
        if self.empty():
            return None
        return self.data[0]

    # Who is index x's parent?
    def parent(self, x):
        return math.floor((x - 1) / 2)

    # Who is index x's left child?
    def left_child(self, x):
        return (x + 1) * 2 - 1

    # Who is index x's right child?
    def right_child(self, x):
        return (x + 1) * 2

    # Swap the values at index x and y
    def swap(self, x, y):
        temp = self.data[x]
        self.data[x] = self.data[y]
        self.data[y] = temp

    # Insert a new number x
    # If no space, ignore and make no changes
    def insert(self, x):
        if len(self.data) == self.max_size:
            return
        else:
            self.data.append(x)
            self.current_size += 1

    # Upheap starting at index i
    def upheap(self, i):
        if self.parent(i) < 0:
            return
        p = self.data[self.parent(i)]
        if p <= self.data[i]:
            return
        self.swap(i, self.parent(i))
        self.upheap(self.parent(i))

    # Delete the Min and fix heap
    def deletemin(self):
        self.swap(0, self.current_size - 1)
        self.current_size = self.current_size - 1
        self.downheap(0)

    # Downheap starting at index i
    def downheap(self, i):
        if (self.data[self.left_child(i)] == None) or (self.data[self.right_child(i)] == None):
            return

        if self.data[self.left_child(i)] != None and (self.data[self.right_child(i)] == None):
            children = [self.data[self.left_child(i)]]
            m = self.left_child(i)
        elif self.data[self.left_child(i)] == None and (self.data[self.right_child(i)] != None):
            children = [self.data[self.right_child(i)]]
            m = self.right_child(i)
        else:
            children = [self.data[self.left_child(i)], self.data[self.right_child(i)]]
            if self.data[self.left_child(i)] < self.data[self.right_child(i)]:
                m = self.left_child(i)
            else:
                m = self.right_child(i)

        for child in children:
            if self.data[i] <= child:
                pass
            return

        self.swap(i, m)
        self.downheap(m)


# Implement a Heapsort
def heapsort(A):
    P = Heap(len(A))
    for i in range(len(A)):
        P.insert(A[i])
    for i in range(len(A)):
        A[i] = P.min()
        P.deletemin()


# Run the exact Experiment from the Slides
if __name__ == "__main__":
    H = Heap(10)
    X = [79, 87, 28, 6, 46, 66, 17, 1, 58, 94]
    for val in X:
        H.insert(val)
        print(H)
    # Now Delete them all
    while not H.empty():
        print("Delete:", H.min())
        H.deletemin()
        print(H)
    # Test Heapsort
    print("X before Heapsort:", X)
    heapsort(X)
    print("X after Heapsort:", X)
