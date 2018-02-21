inp = input("Sk:")
br1 = ["  --- "]
br2 = ["--- "]
linija = br1 + br2 * (int(inp) - 1) + ["\n"]
rodlin = "".join(linija)

sles = [" | "]
vrb = [inp]
ln1 = sles + vrb
ln2 = ln1 * int(inp) + [" |"] + ["\n"]
pirm = "".join(ln2)

bendras = (rodlin + pirm) * int(inp) + rodlin
print(bendras)
