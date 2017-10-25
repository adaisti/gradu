import argparse

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
	parser.add_argument("--type", "-t", type=str, required=True)

	args = parser.parse_args()
	print_words(args)


		


if __name__ == '__main__':
	main()