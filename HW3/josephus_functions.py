# Mark Boady CS 260 - Drexel University 2021
from collections import deque


# Josephus
# Implemented using the builtin list as the queue
def josephus_list(n, m):
    return []


# Implemented using the deque object from collections
def josephus_deque(n, m):
    return []


# Implemented using a handmade Queue DS using the provided
# Node clas and template
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
        return None

    # Check if the queue is empty
    def empty(self):
        return False

    # Add a new value to the end of the queue
    def enqueue(self, v):
        return

    # Remove the first element from the queue
    # return the value you removed
    # If the queue is empty, return None and do nothing
    def dequeue(self):
        return None


# Implemented using the objects you implemented above
def josephus_node(n, m):
    return []
