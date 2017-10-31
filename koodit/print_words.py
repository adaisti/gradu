import argparse

def print_words(args):
	f = open(args.file)
	lines = f.read()
	
	for line in lines.split("\n"):
		if line == "":
			continue
		word1 = line.split("\t")[3]
		word2 = line.split("\t")[4]
		print(word1.lower())
		print(word2.lower())


def main():
	parser = argparse.ArgumentParser()                                               

	parser.add_argument("--file", "-f", type=str, required=True)
	args = parser.parse_args()
	print_words(args)


		


if __name__ == '__main__':
	main()