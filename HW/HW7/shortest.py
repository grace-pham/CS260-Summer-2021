import heapq


def read_graph(input_file):
    file = open(input_file, 'r')

    lines = file.readlines()
    number_of_nodes = int(lines[0][0])
    G = [[float("inf") for i in range(number_of_nodes)] for j in range(number_of_nodes)]

    for line in lines[1:]:
        data = line.split(" ")

        from_node = int(data[0])
        to_node = int(data[1])
        weight = float(data[2])

        G[from_node][to_node] = weight
    return G


def dijkstra(G, start_node):
    d = [float("inf") for i in range(len(G))]
    d[start_node] = 0.0
    Q = []
    for (node, distance) in enumerate(d):
        heapq.heappush(Q, (distance, node))

    nodes_done = 0
    while Q != []:
        u = Q[0][1]
        heapq.heappop(Q)

        adjList = []
        for (index, adjNode) in enumerate(G[u]):
            if adjNode != float("inf"):
                adjList.append(index)

        for v in adjList:
            if d[v] > (d[u] + G[u][v]):
                d[v] = d[u] + G[u][v]
                heapq.heappush(Q, (d[v], v))
        nodes_done += 1
    return d


def help():
    print("Possible Commands are:")
    print("dijkstra x - Runs Dijkstra starting at node X. X must be an integer")
    print("help - prints this menu")
    print("exit or ctrl-d - Exit the program")


def exit_program():
    print("Bye")
    exit()


def run_program(input_file):
    while True:
        help()
        command = input("Enter command:\n")
        if command == "help":
            help()
        elif command == "exit":
            exit_program()
        elif command.startswith("dijkstra "):
            x = command.split(" ")[-1]
            if not isinstance(int(x), int):
                print('Please enter "dijkstra x", where x must be integer')
            else:
                G = read_graph(input_file)
                print(dijkstra(G, int(x)))
        else:
            print("Invalid command. Please enter one of the possible commands!")


if __name__ == "__main__":
    input_file = input("File containing graph:\n")
    run_program(input_file=input_file)
