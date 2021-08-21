import heapq


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
        count_line += 1
    return G

def prim(G, start_node):
    T = {float("inf") for i in range(G[1])}
    edges = []
    U = {start_node}

    # Add Edges to Priority Queue that are adjacent to start node
    for (node, distance) in enumerate(G[start_node]):
        heapq.heappush(edges, (distance, node))

    heapq.heappush(edges, G[0][start_node])
    while U != G[1]:
        (u, v) = (0, 0)  # ???
        T = T.union({(u, v)})
        U = U.union({v})
    return T


def kruskal(G):
    pass


def help():
    print("Commands:")
    print("exit or ctrl-d - Exit the program")
    print("help - prints this menu")
    print("prim x - Runs Pim's Algorithm starting at node X. X must be an integer")
    print("kruskal - Runs Kruskal's algorithm")


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
        else:
            G = read_graph(input_file)
            if command == "kruskal":
                print(kruskal(G))
            elif command.startswith("prim "):
                x = command.split(" ")[-1]
                if not isinstance(int(x), int):
                    print('Please enter "prim x", where x must be integer')
                else:
                    print(prim(G, int(x)))
            else:
                print("Invalid command. Please enter one of the possible commands!")


if __name__ == "__main__":
    # print("Welcome to Minimum Spanning Tree Finder")
    # input_file = input("Give the file name graph is in:\n")
    # run_program(input_file=input_file)

    print(read_graph("input1.txt"))
