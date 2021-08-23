def postfix(input_list):
    L = []

    if len(input_list) == 0:
        raise Exception("Empty input list")

    for i in input_list:
        if str(i).isnumeric():
            L.append(i)
        elif i == "+":
            value_1 = L.pop()
            value_2 = L.pop()
            total = value_1 + value_2
            L.append(total)
        elif i == "*":
            value_1 = L.pop()
            value_2 = L.pop()
            product = value_1 * value_2
            L.append(product)
        else:
            raise Exception("Invalid element in input list")

    return L[-1]


if __name__ == "__main__":
    # Test with 2 input lists given in the question
    A = [1, 7, "+", 9, 5, 6, "*", "+", "*"]
    print(postfix(A))
    B = [3, 4, 7, "*", "+"]
    print(postfix(B))
