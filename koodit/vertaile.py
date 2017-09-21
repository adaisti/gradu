#!/usr/bin/env python
# -*- coding: utf-8 -*-





#1. tee funktio, joka hakee listan sukulaissanoista ontologiasta
#2. sellainen, joka hakee saman fasttextistä
#3. funktio, joka vertaa 1. ja 2. tuloksia
#4. koodaa silmukka, jossa vaihdetaan fasttextin parametreja
#2. pitäisi mennä näin:
#subprocess.check_output("fasttextkomento").split("\n").split(" ")

import subprocess
from scipy.spatial.distance import cosine
from scipy.stats import spearmanr
import numpy as np

def main():
	#f = open('set2_kaannos_utf-8.tsv', 'r')
	#lines = f.read()

	#for line in lines.split("\n"):
	#	word1 = line.split("\t")[3]
	#	word2 = line.split("\t")[4] 
	#	word1 = "".join(word1.split())
	#	word2 = "".join(word2.split())
	#	print(word1, word2) 

	f = open('set2_vectors.txt', 'r')
	lines = f.read()

	vectors = []

	for line in lines.split("\n"):
		vector = np.array(line.split()[1:], dtype=float)
		vectors.append(vector)



	scores = []

	f2 = open('set2_kaannos_utf-8.tsv', 'r')
	lines2 = f2.read()

	for line in lines2.split("\n"):
		score = line.split("\t")[2]
		scores.append(score)

	similarities = []

	for i in range(0,len(vectors) - 2,2):
		similarities.append(1 - cosine(vectors[i], vectors[i + 1]))

	similarities = similarities[1:]	#1 koska eka rivi on sellainen turha
	scores = scores[1:]#

	#for i in range(0, len(similarities)):	
	#	print(similarities[i], scores[i])

	scores = np.array(scores)

	#np.isfinite(similarities).any()
	#np.isfinite(np.sum(scores))

	print(spearmanr(similarities, scores))






		





	

	





if __name__ == '__main__':
	main()