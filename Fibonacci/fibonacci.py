inp = int(input("Kiek skaičių: "))
a, b = 0, 1
for i in range(inp):
    a, b = b, a + b
    print(a)
