import heapq

my_heap = []

heapq.heappush(my_heap, (7, "Process 3"))
heapq.heappush(my_heap, (2, "Process 9"))
heapq.heappush(my_heap, (0, "OS Task"))

print(f"The first task to do is: {heapq.heappop(my_heap)}")
print(f"The second task to do is: {heapq.heappop(my_heap)}")
print(f"The third task to do is: {heapq.heappop(my_heap)}")
