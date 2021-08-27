import math

a = int(input("Enter Value for a:"))
b = int(input("Enter Value for b:"))
x = int(input("Enter Value for x:"))
y = int(input("Enter Value for y:"))
print(f"Evaluating {a}T(n/{b})+n^{x} log2(n)^{y}")


def T(n):
    if n <= 1:
        return 1
    else:
        return a * T(math.floor(n / b)) + (n ** x) * math.ceil(math.log2(n) ** y)


if __name__ == "__main__":
    n = int(input("Enter Value for n:"))
    print(T(n))
