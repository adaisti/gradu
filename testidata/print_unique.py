import argparse

def print_words(args):
	f = open(args.file)
	lines = f.read()

	lista = []
	
	for line in lines.split("\n"):
		if line == "":
			continue


		if ":" in line:
			for pari in lista:
				print(pari)
			lista = []
			print(line)
			continue


		word1 = line.split()[0]
		word2 = line.split()[1]
		word3 = line.split()[2]
		word4 = line.split()[3]

		pari1 = word1 + " " + word2
		pari2 = word3 + " " + word4

		if not pari1 in lista:
			lista.append(pari1)
		if not pari2 in lista:
			lista.append(pari2)

	
		


def main():
	parser = argparse.ArgumentParser()                                               

	parser.add_argument("--file", "-f", type=str, required=True)
	args = parser.parse_args()
	print_words(args)


		


if __name__ == '__main__':
	main()