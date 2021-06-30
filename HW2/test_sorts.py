# Mark Boady
# Drexel University
# CS 260

# This function generate a random list of
# size
# It sorts using the given sort_fun
# It then checks that the answer is correct
import random


def check_list(sort_fun, size):
    X = [random.randint(-10 * size, 10 * size) for n in range(0, size)]
    T = X[:]  # Make a copy
    sort_fun(T)
    # Is the array sorted?
    for i in range(1, len(T)):
        assert T[i] >= T[i - 1]
    # Are all the elements in the list?
    for num in X:
        assert T.count(num) == X.count(num)
    return


import sort_code


# Built In Sort Tests
def test_builtin_ten():
    check_list(sort_code.builtin, 10)


def test_builtin_hundred():
    check_list(sort_code.builtin, 100)


def test_builtin_thousand():
    check_list(sort_code.builtin, 1000)


def test_builtin_fivethousand():
    check_list(sort_code.builtin, 5000)


# Gnome SORT Tests
def test_gnome_ten():
    check_list(sort_code.gnome, 10)


def test_gnome_hundred():
    check_list(sort_code.gnome, 100)


def test_gnome_thousand():
    check_list(sort_code.gnome, 1000)


def test_gnome_fivethousand():
    check_list(sort_code.gnome, 5000)

# Add your own tests for the new sorts below
