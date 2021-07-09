# Mark Boady CS 260 - Drexel University 2021
from collections import deque


# Josephus
# Implemented using the builtin list as the queue
def josephus_list(n, m):
    Q = []

    # Populate queue list
    for i in range(n):
        Q.append(i)

    kill_list = []

    start_position = 1
    while not len(Q) == 0:
        if start_position == m:
            kill_position = Q.pop(0)
            kill_list.append(kill_position)
            start_position = 1
        else:
            skip_position = Q.pop(0)
            Q.append(skip_position)
            start_position += 1

    return kill_list


# Implemented using the deque object from collections
def josephus_deque(n, m):
    Q = deque()

    # Populate deque
    for i in range(n):
        Q.append(i)

    kill_list = []

    start_position = 1
    while not len(Q) == 0:
        if start_position == m:
            kill_position = Q.popleft()
            kill_list.append(kill_position)
            start_position = 1
        else:
            skip_position = Q.popleft()
            Q.append(skip_position)
            start_position += 1

    return kill_list


# Implemented using a handmade Queue DS using the provided
# Node class and template
class Node:
    def __init__(self, v, n):
        self.value = v
        self.next = n


class Queue:
    # Create an empty queue
    # Both head and tail node should be None
    def __init__(self):
        self.head = None
        self.tail = None

    # Print out the Queue
    # Do whatever you want here.
    # You will want this implemented for testing
    def __str__(self):
        return ""

    # Return the front of the queue
    # or None if the queue is empty
    def front(self):
        if self.empty():
            return None
        return self.head

    # Check if the queue is empty
    def empty(self):
        return self.head == None

    # Add a new value to the end of the queue
    def enqueue(self, v):
        new_node = Node(v, None)
        if self.tail == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    # Remove the first element from the queue
    # return the value you removed
    # If the queue is empty, return None and do nothing
    def dequeue(self):
        if self.empty():
            return None
        v = self.head.value
        self.head = self.head.next
        if self.empty():
            self.tail = None
        return v


# Implemented using the objects you implemented above
def josephus_node(n, m):
    Q = Queue()

    # Populate Queue
    for i in range(n):
        Q.enqueue(i)

    kill_list = []

    start_position = 1
    while not Q.empty():
        if start_position == m:
            kill_position = Q.dequeue()
            kill_list.append(kill_position)
            start_position = 1
        else:
            skip_position = Q.dequeue()
            Q.enqueue(skip_position)
            start_position += 1

    return kill_list
