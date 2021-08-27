import heapq


# Quicksort
def _swap(swapped_list, index_a, index_b):
    temp = swapped_list[index_a]
    swapped_list[index_a] = swapped_list[index_b]
    swapped_list[index_b] = temp


def _partition(input_list, start, stop):
    pivot = input_list[stop]
    i = start
    for j in range(start, stop):
        if input_list[j] <= pivot:
            _swap(input_list, i, j)
            i += 1
    _swap(input_list, i, stop)
    return i


def _quick_sort_helper(input_list, start, stop):
    if start < stop:
        p = _partition(input_list, start, stop)
        _quick_sort_helper(input_list, start, p - 1)
        _quick_sort_helper(input_list, p + 1, stop)


def quick_sort(input_list):
    _quick_sort_helper(input_list, 0, len(input_list) - 1)


# Read graph information from file
def _read_file(input_file):
    file = open(input_file, 'r')
    lines = file.readlines()
    return lines


def get_number_of_nodes(input_file):
    lines = _read_file(input_file)
    number_of_nodes = int(lines[0][0])
    return number_of_nodes


def build_graph(input_file):
    lines = _read_file(input_file)
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


# Prim algorithm
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


# Kruskal algorithm
def kruskal(G):
    T = [[float("inf") for i in range(len(G))] for j in range(len(G))]

    S = []
    for (n, n_content) in enumerate(G):
        S.append({n})

    # MWB: This has the same runtime as you had above
    edgeList = []
    for m in range(len(G)):
        for n in range(len(G[m])):
            if G[m][n] != float("inf"):
                edge = (G[m][n], m, n)
                edgeList.append(edge)

    # Sort edges by weights
    quick_sort(edgeList)  # MWB: Same runtime as the stuff I commented

    for i in range(len(edgeList)):  # MWB: Loop over my array
        edge = edgeList[i]
        edge_from = edge[1]  # MWB: from is second
        edge_to = edge[2]  # MWB: to is third
        edge_weight = edge[0]  # MWB: Weight is first
        if S[edge_from] != S[edge_to]:

            T[edge_from][edge_to] = edge_weight
            T[edge_to][edge_from] = edge_weight

            S[edge_from] = S[edge_from].union(S[edge_to])  # MWB: You hardcoded this index :-(
            for node in S[edge_from]:
                S[node] = S[node].union(S[edge_from])

            if edge_from < edge_to:
                print(f"Selected Edge: [{edge_from}, {edge_to}, {edge_weight}]")
            else:
                print(f"Selected Edge: [{edge_to}, {edge_from}, {edge_weight}]")


# Helpers methods for running program
def start_prim(command, G):
    x = command.split(" ")[-1]
    if not isinstance(int(x), int):
        print('Please enter "prim x", where x must be integer')
    else:
        print("Running Prim's Algorithm")
        prim(G, int(x))


def start_kruskal(G):
    print("Running Kruskal's Algorithm")
    kruskal(G)


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
                start_kruskal(G)
            elif command.startswith("prim "):
                start_prim(command, G)
            else:
                print("Invalid command. Please enter one of the possible commands!")


if __name__ == "__main__":
    print("Welcome to Minimum Spanning Tree Finder")
    input_file = input("Give the file name graph is in:\n")
    help()
    run_program(input_file=input_file)
