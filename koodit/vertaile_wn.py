#!/usr/bin/env python
# -*- coding: utf-8 -*-



#ajo-ohje
#ensin print_wordsillä sanat omilla riveillään tiedostoon
#sitten siitä tiedostosta vektoritiedosto fasttextin print-word-vectorsilla  _vectors -tiedostoon
#tällä koodilla siitä vertailut





from scipy.spatial.distance import cosine
from scipy.stats import spearmanr
import numpy as np
import argparse




def correlation(args):


	f = open(args.vectorfile)	
	lines = f.read()

	f2 = open(args.scorefile)
	lines2 = f2.read()

	vectors = []
	words = []
	similarities = []


	for line in lines.split("\n"):
		vector = np.array(line.split()[1:], dtype=float)
		vectors.append(vector)


	for line in lines2.split("\n"):

		if line == "":
			continue

		if args.type in line:
		#if True:



			word1 = line.split("\t")[1]
			word2 = line.split("\t")[3]

			if " " in word1 or " " in word2:
				continue

		#word1 = line.split("\t")[3]
		#word2 = line.split("\t")[4]

			words.append(word1 + " " + word2)


	for i in range(0,len(vectors) - 2,2):
		similarities.append(1 - cosine(vectors[i], vectors[i + 1]))

	similarities = similarities[1:]	#1 koska eka rivi on sellainen turha
	words = words[1:]

	max_sim = 0
	max_w = ""
	min_sim = 10
	min_w = ""


	for i in range(0, len(similarities)):
		sim = similarities[i]
		w = words[i]
		#if sim > max_sim and w.split()[0].lower() not in  w.split()[1].lower() and w.split()[1].lower() not in  w.split()[0].lower():
		if sim > max_sim and w.split()[0].lower() not in  w.split()[1].lower() and w.split()[1].lower() not in  w.split()[0].lower():
			max_sim = sim
			max_w = w
		if sim < min_sim:
			min_sim = sim
			min_w = w




	print("var", np.var(similarities))
	print("mean", np.mean(similarities))
	print("min", min_sim, min_w)
	print("max", max_sim, max_w)



def main():
	parser = argparse.ArgumentParser()                                               

	parser.add_argument("--vectorfile", "-v", type=str, required=True)
	parser.add_argument("--scorefile", "-s", type=str, required=True)
	parser.add_argument("--type", "-t", type=str, required=True)
	args = parser.parse_args()
	correlation(args)




if __name__ == '__main__':
	main()