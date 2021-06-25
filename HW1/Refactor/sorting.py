# Student: Grace Pham - ntp33 - Course: CS 260
# Script Purpose: Plotting the functions to identify their growth rates using matplotlib


import matplotlib.pyplot as plt

'''
Instruction on installing matplotlib library:
- Open terminal
- Install pip (if not installed)
- Run command: "pip install matplotlib" on terminal
'''

from result_table import *


# Function for plotting the function result
def plot_result(index_list, value_list, graph_title):
    graph = df.pivot_table(index=index_list, values=value_list).plot()
    plt.title(graph_title)
    plt.show()


# Plot result lists of all 12 functions using pandas pivot_table
plot_result(index_list=x_list, value_list=df.columns, graph_title="Graph 0")

# f4_result line grows the fastest compared to other lines, so we exclude f4 out of the values for the plot
# Plot the remaining result lists
plot_result(index_list=x_list,
            value_list=['f1', 'f2', 'f3', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12'],
            graph_title="Graph 1")

# f1_result line grows the fastest compared to other lines, so we exclude f1 out of the values for the plot
# Plot the remaining result lists
plot_result(index_list=x_list,
            value_list=['f2', 'f3', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12'],
            graph_title="Graph 2")

# f9_result line grows the fastest compared to other lines, so we exclude f9 out of the values for the plot
# Plot the remaining result lists
plot_result(index_list=x_list,
            value_list=['f2', 'f3', 'f5', 'f6', 'f7', 'f8', 'f10', 'f11', 'f12'],
            graph_title="Graph 3")

# f3_result line grows the fastest compared to other lines, so we exclude f3 out of the values for the plot
# Plot the remaining result lists
plot_result(index_list=x_list,
            value_list=['f2', 'f5', 'f6', 'f7', 'f8', 'f10', 'f11', 'f12'],
            graph_title="Graph 4")

# f10_result line grows the fastest compared to other lines, so we exclude f10 out of the values for the plot
# Plot the remaining result lists
plot_result(index_list=x_list,
            value_list=['f2', 'f5', 'f6', 'f7', 'f8', 'f11', 'f12'],
            graph_title="Graph 5")

# f11_result line grows the fastest compared to other lines, so we exclude f11 out of the values for the plot
# Plot the remaining result lists
plot_result(index_list=x_list,
            value_list=['f2', 'f5', 'f6', 'f7', 'f8', 'f12'],
            graph_title="Graph 6")

# From the plot result in Graph 6, we can conclude the order of growth rate in ascending order is f12, f8, f2, f7, f5

# Combining results from Graph 6 and from Tables 0, 1, 2, 3, 4, and 5, we can conclude that the order of growth rates
# for all functions in ascending order is f12, f8, f2, f7, f5, f11, f10, f3, f9, f1, f4
