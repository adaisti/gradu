import argparse

# Tämä liittyy oikeasti analogioihin
def print_single(args):
	f = open(args.file)
	lines = f.read()

	words = []
	
	for line in lines.split("\n"):
		if line == "" or ":" in line:
			continue

		word1 = line.split()[0]
		word2 = line.split()[1]
		w1 = word1.lower()
		w2 = word2.lower()

		if w1 not in words:
			words.append(w1)

		if w2 not in words:
			words.append(w2)

	for w in words:
		print(w)


def print_words(args):
	f = open(args.file)
	lines = f.read()
	
	for line in lines.split("\n"):
		if line == "":
			continue

		if args.type in line:

			word1 = line.split("\t")[1]
			word2 = line.split("\t")[3]

			if " " in word1 or " " in word2:
				continue

			print(word1.lower())
			print(word2.lower())


def main():
	parser = argparse.ArgumentParser()                                               

	parser.add_argument("--file", "-f", type=str, required=True)
#	parser.add_argument("--type", "-t", type=str, required=True)

	args = parser.parse_args()
	print_single(args)


		


if __name__ == '__main__':
	main()