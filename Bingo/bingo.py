
import random

pilnas = [i for i in range(1, 101)]
nepilnas = []

for k in range(90):
	while len(nepilnas) < 90:
		a = random.randint(1, 100)
		if a not in nepilnas:
			nepilnas.append(a)

for k in nepilnas:
	for t, v in enumerate(pilnas):
		if k != v:
			pilnas[k - 1] = "__"

nets = False
tss = False

while True:
	if len(set(pilnas)) != 1:
		bingo = """
Bingo!
Jūsų skačiai:
{} {} {} {} {} {} {} {} {} {}\n
{} {} {} {} {} {} {} {} {} {}\n
{} {} {} {} {} {} {} {} {} {}\n
{} {} {} {} {} {} {} {} {} {}\n
{} {} {} {} {} {} {} {} {} {}\n
{} {} {} {} {} {} {} {} {} {}\n
{} {} {} {} {} {} {} {} {} {}\n
{} {} {} {} {} {} {} {} {} {}\n
{} {} {} {} {} {} {} {} {} {}\n
{} {} {} {} {} {} {} {} {} {}\n
Įveskite skaičių ir jis bus pašalintas, norėdami baigti anskčiau suveskite "baigti"
""".format(*pilnas)
		print(bingo)

		if nets is True:
			print("Ne tas skaičius")
		else:
			pass

		if tss is True:
			print("Turite suvesti skaičių")
		else:
			pass

		inp = input("Skaičius:")

		if inp == "baigti":
			break
		elif inp != "baigti" and inp.isalpha():
			tss = True
		else:
			tss = False
			if int(inp) in pilnas:
				for k, v in enumerate(pilnas):
					if v != "__":
						if v == int(inp):
							pilnas.pop(k)
							pilnas.insert(k, "__")
							nets = False
					else:
						pass
			else:
				nets = True

	else:
		print("Jūs laimėjote")
		break










