
# coding: utf-8

br1 = ["  --- "]
br2 = ["--- "]
linija = br1 + br2 * 2 + ["\n"]
rodlin = "".join(linija)

sles = [" | "]

vrb = [["1"], ["2"], ["3"], ["4"], ["5"], ["6"], ["7"], ["8"], ["9"]]


def upd(lis):
    vrb = lis
    ln1 = sles + vrb[0] + sles + vrb[1] + sles + vrb[2] + [" |"] + ["\n"]
    sln1 = "".join(ln1)

    ln2 = sles + vrb[3] + sles + vrb[4] + sles + vrb[5] + [" |"] + ["\n"]
    sln2 = "".join(ln2)

    ln3 = sles + vrb[6] + sles + vrb[7] + sles + vrb[8] + [" |"] + ["\n"]
    sln3 = "".join(ln3)

    bendras = rodlin + sln1 + rodlin + sln2 + rodlin + sln3 + rodlin
    return bendras


print(upd(vrb))

vrb = [["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"], ["_"]]

while True:
    zaid1 = input("1 žaidėjas: įrašykite skaičių: ")
    if int(zaid1) == 1:
        vrb[0] = ["X"]
        print(upd(vrb))
    elif int(zaid1) == 2:
        vrb[1] = ["X"]
        print(upd(vrb))
    elif int(zaid1) == 3:
        vrb[2] = ["X"]
        print(upd(vrb))
    elif int(zaid1) == 4:
        vrb[3] = ["X"]
        print(upd(vrb))
    elif int(zaid1) == 5:
        vrb[4] = ["X"]
        print(upd(vrb))
    elif int(zaid1) == 6:
        vrb[5] = ["X"]
        print(upd(vrb))
    elif int(zaid1) == 7:
        vrb[6] = ["X"]
        print(upd(vrb))
    elif int(zaid1) == 8:
        vrb[7] = ["X"]
        print(upd(vrb))
    elif int(zaid1) == 9:
        vrb[8] = ["X"]
        print(upd(vrb))

    if ((vrb[0] == vrb[1] == vrb[2] == ["X"]) or
        (vrb[3] == vrb[4] == vrb[5] == ["X"]) or
        (vrb[6] == vrb[7] == vrb[8] == ["X"]) or
        (vrb[0] == vrb[3] == vrb[6] == ["X"]) or
        (vrb[1] == vrb[4] == vrb[7] == ["X"]) or
        (vrb[2] == vrb[5] == vrb[8] == ["X"]) or
        (vrb[0] == vrb[4] == vrb[8] == ["X"]) or
        (vrb[3] == vrb[4] == vrb[6] == ["X"])):
        print("Laimėjo 1 žaidėjas")
        break

    zaid2 = input("2 žaidėjas: įrašykite skaičių: ")
    if int(zaid2) == 1:
        vrb[0] = ["O"]
        print(upd(vrb))
    elif int(zaid2) == 2:
        vrb[1] = ["O"]
        print(upd(vrb))
    elif int(zaid2) == 3:
        vrb[2] = ["O"]
        print(upd(vrb))
    elif int(zaid2) == 4:
        vrb[3] = ["O"]
        print(upd(vrb))
    elif int(zaid2) == 5:
        vrb[4] = ["O"]
        print(upd(vrb))
    elif int(zaid2) == 6:
        vrb[5] = ["O"]
        print(upd(vrb))
    elif int(zaid2) == 7:
        vrb[6] = ["O"]
        print(upd(vrb))
    elif int(zaid2) == 8:
        vrb[7] = ["O"]
        print(upd(vrb))
    elif int(zaid2) == 9:
        vrb[8] = ["O"]
        print(upd(vrb))

    if ((vrb[0] == vrb[1] == vrb[2] == ["O"]) or
        (vrb[3] == vrb[4] == vrb[5] == ["O"]) or
        (vrb[6] == vrb[7] == vrb[8] == ["O"]) or
        (vrb[0] == vrb[3] == vrb[6] == ["O"]) or
        (vrb[1] == vrb[4] == vrb[7] == ["O"]) or
        (vrb[2] == vrb[5] == vrb[8] == ["O"]) or
        (vrb[0] == vrb[4] == vrb[8] == ["O"]) or
        (vrb[3] == vrb[4] == vrb[6] == ["O"])):
        print("Laimėjo 2 žaidėjas")
        break

