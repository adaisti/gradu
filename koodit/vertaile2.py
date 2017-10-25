#!/usr/bin/env python
# -*- coding: utf-8 -*-



#ajo-ohje
#ensin print_wordsillä sanat omilla riveillään tiedostoon
#sitten siitä tiedostosta vektoritiedosto fasttextin print-word-vectorsilla  _vectors -tiedostoon
#tällä koodilla siitä vertailut




#varmista että skripti tekee mitä pitääkin
#jos ei niin lähetetään meiliä
#vastausta odotellessa mennään sitten tällä: yritetään saada itse opetettu samantasoiseksi kuin netistä ladattu


#from __future__ import print_function

from scipy.spatial.distance import cosine
from scipy.stats import spearmanr
import numpy as np
import argparse



def correlation(args):

	
	f = open(args.vectorfile)	
	lines = f.read()

	f2 = open(args.scorefile)
	lines2 = f2.read()


	f3 = open(args.vectorfile2)
	lines3 = f3.read()

	vectors = []
	vectors2 = []
	scores = []
	words = []
	
	similarities = []
	#similarities = np.empty(2034)
	similarities2 = []


	for line in lines.split("\n"):
		vector = np.array(line.split()[1:], dtype=float)
		vectors.append(vector)


	for line in lines3.split("\n"):
		vector = np.array(line.split()[1:], dtype=float)
		vectors2.append(vector)

	for line in lines2.split("\n"):

		if line == "":
			continue

		score = line.split("\t")[2]
		scores.append(score)
		word1 = line.split("\t")[0]
		word2 = line.split("\t")[1]

		#word1 = line.split("\t")[3]
		#word2 = line.split("\t")[4]

		words.append(word1 + " " + word2)



# for v1, v2 in zip(vectors, vectors[1: ] )
# for v1, v2 in zip(vectors[::2], vectors[1::2 ] )



	for i in range(0, len(vectors) - 1, 2):
		similarities.append(1 - cosine(vectors[i], vectors[i + 1]))
		#np.append(similarities, 1 - cosine(vectors[i], vectors[i + 1]))
		#print(vectors[i])
		#print(vectors[i + 1])

		#print(cosine(vectors[i], vectors[i + 1]))
		#print(similarities)


	for i in range(0, len(vectors) - 1, 2):
		similarities2.append(1 - cosine(vectors2[i], vectors2[i + 1]))

	#similarities = similarities[1:]	#1 koska eka rivi on sellainen turha
	#similarities2 = similarities2[1:]
	#scores = scores[1:]
	#words = words[1:]

	amount = 0

	pairs = {}

	for i in range(0, len(similarities)):	
		#print(words[i], similarities[i], scores[i])

		d = 0.25

		#pairs[similarities[i]] = words[i]
		#if not (similarities2[i] < similarities[i] + d and similarities2[i] > similarities[i] - d):
		#	print(words[i], similarities[i], similarities2[i], scores[i])


		#if similarities2[i] < similarities[i]:
		#	print(words[i], similarities[i], similarities2[i], scores[i])
		#	amount += 1
	scores = np.array(scores)


#	for key in sorted(pairs):
#		print(key, pairs[key])

	print(len(similarities))
	print(len(scores))
#	print(similarities2)
#	print(scores)

	print(spearmanr(similarities, scores))
#	print(spearmanr(similarities2, scores))
#	print(amount/len(similarities))



def main():
	parser = argparse.ArgumentParser()                                               

	parser.add_argument("--vectorfile", "-v", type=str, required=True)
	parser.add_argument("--vectorfile2", "-v2", type=str, required=True)
	parser.add_argument("--scorefile", "-s", type=str, required=True)
	args = parser.parse_args()
	correlation(args)




if __name__ == '__main__':
	main()