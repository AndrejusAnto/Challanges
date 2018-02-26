def sum67(list1):
    while True:
        c = list1
        if 6 not in c:
            for k, v in enumerate(c):
                if v == 7:
                    c.pop(k)
            print("Bendra suma", sum(c))
            break
        else:
            for k1, v1 in enumerate(c):
                if v1 == 6:
                    b = c[:k1]
                    d = c[(k1 + 1):]
                    list1 = b + d
                    for k2, v2 in enumerate(d):
                        if v2 == 7:
                            e = d[(k2 + 1):]
                            list1 = b + e
                            c = list1
