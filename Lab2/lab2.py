import random
import timeit
import pandas as pd

SETUP_CODE = '''
from functions import pow1, pow2, pow3
'''

TEST_CODE1 = '''
pow1(a,b)
'''

TEST_CODE2 = '''
pow2(a,b)
'''

TEST_CODE3 = '''
pow3(a,b)
'''

a_list = []
b_list = []
runtime_pow1 = []
runtime_pow2 = []
runtime_pow3 = []

for i in range(0, 15):
    times_to_repeat = 3
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    t1 = timeit.repeat(
        TEST_CODE1,
        f"a={str(a)}\nb={str(b)}\n{SETUP_CODE}",
        repeat=times_to_repeat,
        number=10000
    )

    t2 = timeit.repeat(
        TEST_CODE2,
        f"a={str(a)}\nb={str(b)}\n{SETUP_CODE}",
        repeat=times_to_repeat,
        number=10000
    )

    t3 = timeit.repeat(
        TEST_CODE3,
        f"a={str(a)}\nb={str(b)}\n{SETUP_CODE}",
        repeat=times_to_repeat,
        number=10000
    )

    runtime1 = sum(t1) / len(t1)
    runtime2 = sum(t2) / len(t2)
    runtime3 = sum(t3) / len(t3)

    a_list.append(a)
    b_list.append(b)
    runtime_pow1.append(runtime1)
    runtime_pow2.append(runtime2)
    runtime_pow3.append(runtime3)

df = pd.DataFrame(list(zip(a_list, b_list, runtime_pow1, runtime_pow2, runtime_pow3)),
                  columns=['a', 'b', 'runtime_pow1', 'runtime_pow2', 'runtime_pow3'])
print(df)
