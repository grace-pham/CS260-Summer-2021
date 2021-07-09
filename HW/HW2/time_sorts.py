# Mark Boady
# Drexel University
# CS 260

# This is just a starting point.
# It times the first two sorts.

# Extend this code to handle the 4 new sorts.
# Some sorts will take to long and you will
# have to stop them earlier than others.

# Time Two Sorts
import random
import timeit


# Generate a Random Array of Numbers to sort
def rand_array(size):
    return [random.randint(-2 * size, 2 * size) for n in range(0, size)]


# Test the given sort on a random array of size given.
def test_a_sort(sort_name, size):
    setup = "from sort_code import " + sort_name + "\n"
    setup += "from __main__ import rand_array\n"
    setup += "size=" + str(size) + "\n"
    setup += "A=rand_array(size)\n"
    test_code = sort_name + "(A.copy())"
    # You might need to change these parameters
    t = timeit.timeit(test_code, setup, number=100)
    return t


if __name__ == "__main__":
    # Print out the results.
    print("Size | Built In    |    Gnome    |  BubbleSort  | InsertionSort |  MergeSort  |  QuickSort |")
    for x in range(0, 9):
        rowTemplate = "{:4d} | {:11.5} | {:11.5f} | {:11.5f}  |  {:11.5f}  | {:11.5f} | {:11.5f}|"
        built = test_a_sort("builtin", 2 ** x)
        gnome = test_a_sort("gnome", 2 ** x)
        bubble = test_a_sort("bubble_sort", 2 ** x)
        insertion = test_a_sort("insertion_sort", 2 ** x)
        merge = test_a_sort("merge_sort", 2 ** x)
        quick = test_a_sort("quick_sort", 2 ** x)

        print(rowTemplate.format(2 ** x, built, gnome, bubble, insertion, merge, quick))
