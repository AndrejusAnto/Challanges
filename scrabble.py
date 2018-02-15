
# coding: utf-8

scores = {
    "a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
    "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, "l": 1,
    "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
    "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
    "x": 8, "z": 10}

inp = input("Įveskite raides: ").upper()
inp = list(inp)

valid_word = []

with open("sowpods.txt") as f:
    for word in f:
        word = word.strip()
        inp1 = inp.copy()
        alist = []
        for k in word:
            if k in inp1:
                alist.append(k)
                inp1.remove(k)
        if alist == list(word):
            valid_word.append(word)

final = {}
for n in valid_word:
    score = []
    for f in n:
        for k, v in scores.items():
            if k.upper() in f:
                score.append(v)
                final[n] = sum(score)

for key, value in reversed(sorted(final.items(), key=lambda x: x[1])):
    print(key, value)

