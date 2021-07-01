# Mark Boady - CS 260
# Drexel University

# Implement the sorts from lecture in this file.

# Here are two example sorts to start off with.

# These functions have no return values.
# They sort the array in place.

# The built in sort is probably optimal.
def builtin(A):
    A.sort()
    return


# Gnome sort is pretty weird.
# It is like a bad version of insertion sort
# Read more:https://en.wikipedia.org/wiki/Gnome_sort
def gnome(A):
    # Current index in the array
    i = 0
    # While we haven't made it to the end
    while i < len(A):
        # We cannot compare at 0
        # Otherwise check order is correct
        if i == 0 or A[i] >= A[i - 1]:
            i += 1  # Move forward
        else:
            # Swap values
            temp = A[i]
            A[i] = A[i - 1]
            A[i - 1] = temp
            # Go back one and try again
            i -= 1
    return


# Implement the sorts from class below!

def swap(swapped_list, index_a, index_b):
    temp = swapped_list[index_a]
    swapped_list[index_a] = swapped_list[index_b]
    swapped_list[index_b] = temp


def partition(input_list, start, stop):
    pivot = input_list[stop]
    i = start
    for j in range(start, stop):
        if input_list[j] <= pivot:
            swap(input_list, i, j)
            i += 1
    swap(input_list, i, stop)
    return i


def bubble_sort(input_list):
    swapped = 1
    while swapped == 1:
        swapped = 0
        i = 1
        while i < len(input_list):
            if input_list[i - 1] > input_list[i]:
                swap(input_list, i - 1, i)
                swapped = 1
            i += 1


def insertion_sort(input_list):
    i = 1
    while i < len(input_list):
        j = i
        while j > 0 and input_list[j - 1] > input_list[j]:
            swap(input_list, j - 1, j)
            j = j - 1
        i += 1


def merge(input_list, start, middle, stop):
    aux_list = input_list
    i = start
    j = middle + 1
    for k in range(start, stop + 1):
        if i > middle:
            input_list[k] = aux_list[j]
            j += 1
        elif j > stop:
            input_list[k] = aux_list[i]
            i += 1
        elif aux_list[j] > aux_list[i]:
            input_list[k] = aux_list[i]
            i += 1
        else:
            input_list[k] = aux_list[j]
            j += 1


def merge_sort_helper(input_list, start, stop):
    if start >= stop:
        return
    middle = start + (stop - start) // 2
    merge_sort_helper(input_list, start, middle)
    merge_sort_helper(input_list, middle + 1, stop)

    merge(input_list, start, middle, stop)


def merge_sort(input_list):
    merge_sort_helper(input_list, 0, len(input_list) - 1)


def quick_sort(input_list):
    quick_sort_helper(input_list, 0, len(input_list) - 1)


def quick_sort_helper(input_list, start, stop):
    if start < stop:
        p = partition(input_list, start, stop)
        quick_sort_helper(input_list, start, p - 1)
        quick_sort_helper(input_list, p + 1, stop)


def partition(input_list, start, stop):
    pivot = input_list[stop]
    i = start
    for j in range(start, stop):
        if input_list[j] <= pivot:
            swap(input_list, i, j)
            i += 1
    swap(input_list, i, stop)
    return i
