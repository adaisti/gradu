import argparse

def print_words(args):
	f = open(args.file)
	lines = f.read()

	lista = []
	lista2 = []
	
	for line in lines.split("\n"):
		if line == "":
			continue


		if ":" in line:
			lista2 = lista
			#print(lista)
			#print(lista2)


			for pari in lista:
				

				print(len(lista2))
				print(len(lista))

				if lista2 is not None:
					continue
					for pari2 in lista2:
						if not pari == pari2:
							print(pari, pari2)
				lista2 = lista2.remove(pari)



			lista = []
			continue



		word1 = line.split()[0]
		word2 = line.split()[1]

		pari = word1 + " " + word2

		lista.append(pari)

	return

	lista2 = lista
	for pari in lista:
		for pari2 in lista2:
			if not pari == pari2:
				print(pari, pari2)
		lista2 = lista2.remove(pari)
		


def main():
	parser = argparse.ArgumentParser()                                               

	parser.add_argument("--file", "-f", type=str, required=True)
	args = parser.parse_args()
	print_words(args)


		


if __name__ == '__main__':
	main()