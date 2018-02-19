inp = int(input("Kiek skaičių: "))


def fibonacci(sk):
    a = [0, 1]
    for i in range(2, (sk + 1)):
        b = a[-2] + a[-1]
        a.append(b)

    for i in a[1:]:
        print(i)


fibonacci(inp)
