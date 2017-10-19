#!/usr/bin/env python
# -*- coding: utf-8 -*-



#ajo-ohje
#ensin print_wordsillä sanat omilla riveillään tiedostoon
#sitten siitä tiedostosta vektoritiedosto fasttextin print-word-vectorsilla  _vectors -tiedostoon
#tällä koodilla siitä vertailut




#varmista että skripti tekee mitä pitääkin
#jos ei niin lähetetään meiliä
#vastausta odotellessa mennään sitten tällä: yritetään saada itse opetettu samantasoiseksi kuin netistä ladattu



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
	scores = []
	words = []
	similarities = []


	for line in lines.split("\n"):
		vector = np.array(line.split()[1:], dtype=float)
		vectors.append(vector)


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


	for i in range(0,len(vectors) - 2,2):
		similarities.append(1 - cosine(vectors[i], vectors[i + 1]))

	similarities = similarities[1:]	#1 koska eka rivi on sellainen turha
	scores = scores[1:]
	words = words[1:]


	for i in range(0, len(similarities)):	
		#print(words[i], similarities[i], scores[i])

		d = 0.2


		if not (float(scores[i])/10 < similarities[i] + d and float(scores[i])/10 > similarities[i] - d):
			print(words[i], similarities[i], scores[i])

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