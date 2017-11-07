import argparse
import numpy as np
from scipy.stats import spearmanr
from scipy.spatial.distance import cosine



def compare(args):

	vectors = {}

	for line in open(args.vectorfile):
		vector = np.array(line.split()[1:], dtype=float)
		vectors[line.split()[0]] = vector

	d1s = []
	d2s = []

	for line in open(args.file):
		if ":" not in line:
			w1, w2, w3, w4 = line.lower().split()[0:4]

			v1 = np.zeros(300)
			v2 = np.zeros(300)
			v3 = np.zeros(300)
			v4 = np.zeros(300)

			for v in vectors.keys():
				if w1 == v:
					v1 = vectors[v]
				if w2 == v:
					v2 = vectors[v]
				if w3 == v:
					v3 = vectors[v]
				if w4 == v:
					v4 = vectors[v]

			if np.array_equal(v1, np.zeros(300)) or np.array_equal(v2, np.zeros(300)) or np.array_equal(v3, np.zeros(300)) or np.array_equal(v4, np.zeros(300)):
				print("yhyy")

			d1 = np.subtract(v1, v2)
			d2 = np.subtract(v3, v4)
			d1s.append(d1)
			d2s.append(d2)

			sim = 1 - cosine(d1, d2)
			
			if sim > 0.9:
				print(w1, w2, w3, w4, sim)





			

		


def main():
	parser = argparse.ArgumentParser()                                   

	parser.add_argument("--file", "-f", type=str, required=True)
	parser.add_argument("--vectorfile", "-v", type=str, required=True)
	args = parser.parse_args()
	compare(args)


		


if __name__ == '__main__':
	main()