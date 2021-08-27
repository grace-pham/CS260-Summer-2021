import math

print("General Recursion Example")

a = int(input("Enter Value for a:\n"))
b = int(input("Enter Value for b:\n"))
x = int(input("Enter Value for x:\n"))
y = int(input("Enter Value for y:\n"))


def T(n):
    if n <= 1:
        result = 1
    else:
        result = a * T(math.floor(n / b)) + (n ** x) * math.ceil(math.log2(n) ** y)
    return result


if __name__ == "__main__":
    n = int(input("Enter Value for n:\n"))
    print(f"Evaluating {a}T(n/{b})+n^{x} log2(n)^{y}")
    print(f"T({n})={T(n)}")
