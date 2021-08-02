import heapq


def instruction():
    my_heap = []

    heapq.heappush(my_heap, (7, "Process 3"))
    heapq.heappush(my_heap, (2, "Process 9"))
    heapq.heappush(my_heap, (0, "OS Task"))

    print(f"The first task to do is: {heapq.heappop(my_heap)}")
    print(f"The second task to do is: {heapq.heappop(my_heap)}")
    print(f"The third task to do is: {heapq.heappop(my_heap)}")


def heap_sort(arr):
    P = []
    size = len(arr)
    for i in range(size):
        heapq.heappush(P, arr[i])
    for i in range(size):
        arr[i] = heapq.heappop(P)


if __name__ == "__main__":
    test_list_1 = [9, 2, 4, 1, 8, 5, 3]
    heap_sort(test_list_1)
    print(test_list_1)
