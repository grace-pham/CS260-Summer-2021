import matplotlib.pyplot as plt
'''
Instruction on installing matplotlib library:
- Open terminal
- Install pip (if not installed)
- Run command: "pip install matplotlib" on terminal
'''

from result_table import *

# Plot results list using pandas pivot_table
table = df.pivot_table(index=x_list, values=df.columns).plot()
plt.title("Table 0")
plt.show()

# f4_result line grows the fastest compared to other lines, so we exclude f4 out of the values for the plot
# Plot the remaining result lists
table1 = df.pivot_table(index=x_list,
                        values=['f1', 'f2', 'f3', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12']).plot()
plt.title("Table 1")
plt.show()

# f1_result line grows the fastest compared to other lines, so we exclude f1 out of the values for the plot
# Plot the remaining result lists
table2 = df.pivot_table(index=x_list, values=['f2', 'f3', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12']).plot()
plt.title("Table 2")
plt.show()

# f9_result line grows the fastest compared to other lines, so we exclude f9 out of the values for the plot
# Plot the remaining result lists
table3 = df.pivot_table(index=x_list, values=['f2', 'f3', 'f5', 'f6', 'f7', 'f8', 'f10', 'f11', 'f12']).plot()
plt.title("Table 3")
plt.show()

# f3_result line grows the fastest compared to other lines, so we exclude f3 out of the values for the plot
# Plot the remaining result lists
table4 = df.pivot_table(index=x_list, values=['f2', 'f5', 'f6', 'f7', 'f8', 'f10', 'f11', 'f12']).plot()
plt.title("Table 4")
plt.show()

# f10_result line grows the fastest compared to other lines, so we exclude f10 out of the values for the plot
# Plot the remaining result lists
table5 = df.pivot_table(index=x_list, values=['f2', 'f5', 'f6', 'f7', 'f8', 'f11', 'f12']).plot()
plt.title("Table 5")
plt.show()

# f11_result line grows the fastest compared to other lines, so we exclude f11 out of the values for the plot
# Plot the remaining result lists
table6 = df.pivot_table(index=x_list, values=['f2', 'f5', 'f6', 'f7', 'f8', 'f12']).plot()
plt.title("Table 6")
plt.show()

# From the plot result in Table 6, we can conclude the order of growth rate in ascending order is f12, f8, f2, f7, f5

# Combining results from Table 6 and from Tables 0, 1, 2, 3, 4, and 5, we can conclude that the order of growth rates
# for all functions in ascending order is f12, f8, f2, f7, f5, f11, f10, f3, f9, f1, f4
