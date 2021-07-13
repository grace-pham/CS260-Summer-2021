import math
import pandas as pd
import matplotlib.pyplot as plt


def f1(x):
    return x * x * x


def f2(x):
    return math.log2(x)


def f3(x):
    return x * math.log2(x)


def f4(x):
    return (3 / 2) ** x


def f5(x):
    if math.log2(x) == 0:
        return None
    return x / (math.log2(x))


def f6(x):
    return 2 ** x


def f7(x):
    return math.sqrt(x)


def f8(x):
    if math.log2(x) <= 0:
        return None
    return math.log2(math.log2(x))


def f9(x):
    return x ** 2


def f10(x):
    return x


def f11(x):
    return (math.log2(x)) ** 2


def f12(x):
    return (1 / 3) ** x


# Create a list for x(s) to run these fx functions on

x_list = [1, 2, 4, 8, 16, 32, 64]

# Run fx functions with input x_list and store to lists

f1_result = [f1(x) for x in x_list]

f2_result = [f2(x) for x in x_list]

f3_result = [f3(x) for x in x_list]

f4_result = [f4(x) for x in x_list]

f5_result = [f5(x) for x in x_list]

f6_result = [f6(x) for x in x_list]

f7_result = [f7(x) for x in x_list]

f8_result = [f8(x) for x in x_list]

f9_result = [f9(x) for x in x_list]

f10_result = [f10(x) for x in x_list]

f11_result = [f11(x) for x in x_list]

f12_result = [f12(x) for x in x_list]

# Create a dataframe from 12 result lists generated by running functions fx with input x_list
df = pd.DataFrame({
    'f1': f1_result,
    'f2': f2_result,
    'f3': f3_result,
    'f4': f4_result,
    'f5': f5_result,
    'f6': f6_result,
    'f7': f7_result,
    'f8': f8_result,
    'f9': f9_result,
    'f10': f10_result,
    'f11': f11_result,
    'f12': f12_result,
}, index=x_list)

# Plot results list using pandas pivot_table
table = df.pivot_table(index=x_list, values=df.columns).plot()
plt.title("Table 0")
plt.show()

# f4_result line grows the fastest compared to other lines, so we exclude f4 out of the values for the plot
table1 = df.pivot_table(index=x_list,
                        values=['f1', 'f2', 'f3', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12']).plot()
plt.title("Table 1")
plt.show()

# f1_result line grows the fastest compared to other lines, so we exclude f1 out of the values for the plot
table2 = df.pivot_table(index=x_list, values=['f2', 'f3', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12']).plot()
plt.title("Table 2")
plt.show()

# f9_result line grows the fastest compared to other lines, so we exclude f9 out of the values for the plot
table3 = df.pivot_table(index=x_list, values=['f2', 'f3', 'f5', 'f6', 'f7', 'f8', 'f10', 'f11', 'f12']).plot()
plt.title("Table 3")
plt.show()

# f3_result line grows the fastest compared to other lines, so we exclude f3 out of the values for the plot
table4 = df.pivot_table(index=x_list, values=['f2', 'f5', 'f6', 'f7', 'f8', 'f10', 'f11', 'f12']).plot()
plt.title("Table 4")
plt.show()

# f10_result line grows the fastest compared to other lines, so we exclude f10 out of the values for the plot
table5 = df.pivot_table(index=x_list, values=['f2', 'f5', 'f6', 'f7', 'f8', 'f11', 'f12']).plot()
plt.title("Table 5")
plt.show()

# f11_result line grows the fastest compared to other lines, so we exclude f11 out of the values for the plot
table6 = df.pivot_table(index=x_list, values=['f2', 'f5', 'f6', 'f7', 'f8', 'f12']).plot()
plt.title("Table 6")
plt.show()

# From the plot result in Table 6, we can conclude the order of growth rate in ascending order is f12, f8, f2, f7, f5

# Combining results from Table 6 and from Tables 0, 1, 2, 3, 4, and 5, we can conclude that the order of growth rates
# for all functions in ascending order is f12, f8, f2, f7, f5, f11, f10, f3, f9, f1, f4