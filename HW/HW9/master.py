import math

print("Automated Master Theorem")
print("Enter Formula T(n)=a*T(n/b)+n^x*(log2(n)^y)")

a = int(input("Enter Value for a:"))
b = int(input("Enter Value for b:"))
x = int(input("Enter Value for x:"))
y = int(input("Enter Value for y:"))


def master_theorem():
    c = int(math.log(a, b))
    if c > x:
        theta_bound = f"T(n)=Theta(n^{c})"
    elif c < x:
        theta_bound = f"T(n)=Theta(n^{x})"  # f"T(n)=Theta(n^{x} log2(n)^{y})"
    else:
        theta_bound = f"T(n)=Theta(n^{c} log2(n)^{y + 1})"
    return theta_bound


if __name__ == "__main__":
    print(master_theorem())
