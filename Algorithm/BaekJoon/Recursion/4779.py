def blank(n):
    return " " * (3 ** (n - 1))


def recursion(n):
    if n == 0:
        return "-"

    return recursion(n - 1) + blank(n) + recursion(n - 1)


if __name__ == "__main__":
    inputs = []

    while True:
        try:
            inp = input()
            inputs.append(int(inp))
        except:
            break

    for i in inputs:
        print(recursion(i))
