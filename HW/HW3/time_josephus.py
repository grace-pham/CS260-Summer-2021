# Mark Boady CS 260 - Drexel University 2021
import timeit


def run_timing(fun, n, m):
    SETUP = "from josephus_functions import " + fun
    TEST_CODE = fun + "(" + str(n) + "," + str(m) + ")"
    t = timeit.timeit(TEST_CODE, SETUP, number=10000)
    return t


print("| N value | List Ver.  | Deque Ver. | Node Ver.  |")
for i in range(0, 11):
    x = 2 ** i
    t1 = run_timing("josephus_list", x, 2)
    t2 = run_timing("josephus_deque", x, 2)
    t3 = run_timing("josephus_node", x, 2)
    print("| %7d | %10.4f | %10.4f | %10.4f | " % (x, t1, t2, t3))
