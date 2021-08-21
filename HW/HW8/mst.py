import heapq


# Quicksort codes
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


def quick_sort_helper(input_list, start, stop):
    if start < stop:
        p = partition(input_list, start, stop)
        quick_sort_helper(input_list, start, p - 1)
        quick_sort_helper(input_list, p + 1, stop)


def quick_sort(input_list):
    quick_sort_helper(input_list, 0, len(input_list) - 1)


def read_file(input_file):
    file = open(input_file, 'r')
    lines = file.readlines()
    return lines


def get_number_of_nodes(input_file):
    lines = read_file(input_file)
    number_of_nodes = int(lines[0][0])
    return number_of_nodes


def build_graph(input_file):
    lines = read_file(input_file)
    number_of_nodes = get_number_of_nodes(input_file)
    G = [[float("inf") for i in range(number_of_nodes)] for j in range(number_of_nodes)]

    count_line = 0
    for line in lines[1:]:
        data = line.split(" ")

        first_node = int(data[0])
        second_node = int(data[1])
        weight = float(data[2])

        G[first_node][second_node] = weight
        G[second_node][first_node] = weight
        count_line += 1
    return G


def prim(G, start_node):
    print(f"Starting Node: {start_node}")
    T = [[float("inf") for i in range(len(G))] for j in range(len(G))]
    edges = []
    U = {start_node}

    for (node, distance) in enumerate(G[start_node]):
        if distance != float("inf"):
            heapq.heappush(edges, (distance, (start_node, node)))

    while len(U) != len(G):
        min_edge = edges[0][1]
        min_edge_weight = edges[0][0]
        min_edge_from = min_edge[0]
        min_edge_to = min_edge[1]

        heapq.heappop(edges)

        if min_edge_to not in U:
            U.add(min_edge_to)
            print(f"Added {min_edge_to}")
            if min_edge_from > min_edge_to:
                print(f"Using Edge [{min_edge_to}, {min_edge_from}, {min_edge_weight}]")
            else:
                print(f"Using Edge [{min_edge_from}, {min_edge_to}, {min_edge_weight}]")

            T[min_edge_from][min_edge_to] = min_edge_weight
            T[min_edge_to][min_edge_from] = min_edge_weight

            for (node, distance) in enumerate(G[min_edge_to]):
                if distance != float("inf") and node != min_edge_from:
                    heapq.heappush(edges, (distance, (min_edge_to, node)))

    return T


def kruskal(G):
    T = [[float("inf") for i in range(len(G))] for j in range(len(G))]

    S = []
    for (n, n_content) in enumerate(G):
        S.append({n})

    edge_to_weight = {}
    for m in range(len(G)):
        for n in range(len(G[m])):
            if G[m][n] != float("inf"):
                if m < G[m][n]:
                    edge_to_weight[(m, n)] = G[m][n]
                else:
                    edge_to_weight[(n, m)] = G[m][n]

    edges = list(edge_to_weight.keys())
    weights = list(edge_to_weight.values())
    quick_sort(weights)

    edges_sorted = []
    for weight in weights:
        for edge in edges:
            if edge_to_weight[edge] == weight:
                edges_sorted.append(edge)

    for i in range(len(edges_sorted)):
        edge = edges_sorted[i]
        edge_from = edge[0]
        edge_to = edge[1]
        edge_weight = edge_to_weight[edge]

        if S[edge_from] != S[edge_to]:

            T[edge_from][edge_to] = edge_weight
            T[edge_to][edge_from] = edge_weight

            S[edge_from] = S[edge_from].union(S[edge[1]])
            for node in S[edge_from]:
                S[node] = S[node].union(S[edge_from])

            if edge_from < edge_to:
                print(f"Selected Edge: [{edge_from}, {edge_to}, {edge_weight}]")
            else:
                print(f"Selected Edge: [{edge_to}, {edge_from}, {edge_weight}]")


def help():
    print("Commands:")
    print("exit or ctrl-d - Exit the program")
    print("help - prints this menu")
    print("prim integer_value - Runs Prim's Algorithm starting at node given")
    print("kruskal - Runs Kruskal's algorithm")


def exit_program():
    print("Bye")
    exit()


def run_program(input_file):
    while True:
        command = input("Enter command:\n")
        if command == "help":
            help()
        elif command == "exit":
            exit_program()
        else:
            G = build_graph(input_file)
            if command == "kruskal":
                print("Running Kruskal's Algorithm")
                kruskal(G)
            elif command.startswith("prim "):
                x = command.split(" ")[-1]
                if not isinstance(int(x), int):
                    print('Please enter "prim x", where x must be integer')
                else:
                    print("Running Prim's Algorithm")
                    prim(G, int(x))
            else:
                print("Invalid command. Please enter one of the possible commands!")


if __name__ == "__main__":
    print("Welcome to Minimum Spanning Tree Finder")
    input_file = input("Give the file name graph is in:\n")
    help()
    run_program(input_file=input_file)
