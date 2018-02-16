# coding: utf-8
import random
import sys

quizdict = {}
sysfile = sys.argv[1]
with open(str(sysfile)) as f:
    for t in f:
        print(t)
        quiz = t.strip()
        quiz = quiz.split(",")
        quizdict[quiz[0]] = quiz[1]

while True:
    randomk, randomv = random.choice(list(quizdict.items()))
    inputt = input(randomk + "? ")
    if inputt != "baigti":
        if inputt == randomv:
            print("Teisingai")
            print("Norėdami baigti, suveskite 'baigti'")
        else:
            print("Neteisingai")
            print("Norėdami baigti, suveskite 'baigti'")
    else:
        print("Sėkmės")
        break
