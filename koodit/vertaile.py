#!/usr/bin/env python

'''
ajo-ohje
ensin print_wordsillä sanat omilla riveillään tiedostoon
sitten siitä tiedostosta vektoritiedosto fasttextin print-word-vectorsilla  _vectors -tiedostoon
tällä koodilla siitä vertailut
'''

from scipy.spatial.distance import cosine
from scipy.stats import spearmanr
import numpy as np
import argparse


def correlation(args):

	vectors = []
	scores = []
	words = []
	similarities = []

	for line in open(args.vectorfile):
		vector = np.array(line.split()[1:], dtype=float)
		vectors.append(vector)

	for line in open(args.scorefile):

		if line == "":
			continue

		score, word1, word2 = line.split("\t")[2:5]
		scores.append(score)

		words.append(word1 + " " + word2)

	similarities = []

	for i in range(0,len(vectors) - 1, 2):
		if np.all(vectors[i] == 0) or np.all(vectors[i + 1] == 0):
			similarities.append(0)
		else:
			similarities.append(1 - cosine(vectors[i], vectors[i + 1]))

	similarities = similarities[1:]



	for i in range(0, len(similarities)):	
		print(words[i], similarities[i], scores[i])

		d = 0.2

#		if not (float(scores[i])/10 < similarities[i] + d and float(scores[i])/10 > similarities[i] - d):
#			print(words[i], similarities[i], scores[i])

	scores = np.array(scores)

	print(spearmanr(similarities, scores))



def main():
	parser = argparse.ArgumentParser()                                               

	parser.add_argument("--vectorfile", "-v", type=str, required=True)
	parser.add_argument("--scorefile", "-s", type=str, required=True)
	args = parser.parse_args()
	correlation(args)




if __name__ == '__main__':
	main()