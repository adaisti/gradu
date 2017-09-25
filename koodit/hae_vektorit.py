#!/usr/bin/env python
# -*- coding: utf-8 -*-



import subprocess
from scipy.spatial.distance import cosine
from scipy.stats import spearmanr
import numpy as np

def main():
	f = open('/home/adahyvar/gradu/testidata/set2_kaannos_utf-8.tsv', 'r')

	lines = f.read()

	f2 = open('vector_list.txt', 'r')
	
	lines2 = f2.read()

	vectors = []

#	words = []

#	for line in lines.split("\n"):
#		word1 = line.split("\t")[0]
#		word2 = line.split("\t")[1] 
#		word1 = "".join(word1.split())
#		word2 = "".join(word2.split())
#		words.append(word1)
#		words.append(word2)
#

#	with open('/home/adahyvar/fastText/wiki.en.vec', 'r') as infile:
#		for line2 in infile:
#			if line2.split()[0] in words:
#				print(line2)
#

#	return



	scores = []
	similarities = []


	for line in lines.split("\n"):
		word1 = line.split("\t")[0].lower()
		word2 = line.split("\t")[1].lower()
		word1 = "".join(word1.split())
		word2 = "".join(word2.split())
		score = line.split("\t")[2]

		if word1 == "Word1":
			continue
		#print(word1, word2) 
		found1 = False
		found2 = False
		vec1 = ""
		vec2 = ""
		for line2 in lines2.split("\n"):

			if line2 == "":
				continue

			if line2.split()[0] == word1 and "." in line2.split()[1]:
				vec1 =  np.array(line2.split()[1:], dtype=float)
				vectors.append(line2)
				found1 = True
				continue

			if line2.split()[0] == word2 and "." in line2.split()[1]:
				vec2 =  np.array(line2.split()[1:], dtype=float)
				vectors.append(line2)
				found2 = True
				continue

		if found1== False:
			print(word1)
			vectors.append(word1 + " 0")

		if found2== False:
			print(word2)
			vectors.append(word2 + " 0")

		if found1 and found2:
			print(word1, word2, score, 1 - cosine(vec1, vec2))
			scores.append(score)
			similarities.append(1 - cosine(vec1, vec2))




	print(len(vectors))
	print(spearmanr(similarities, scores))

	





if __name__ == '__main__':
	main()


# Jatketaan enkun tutkimista niin, että otetaan joku kokonainen niistä käytetyistä dataseteistä, että saadaan oikeasti
# vertailukelpoinen juttu. Tästä puuttuu sanoja. Ja muutenkin olisi vain puolet sanoista.

#Selvitetään onko paperissa käytetty spearman rank (esim. 74) nyt sama kuin 0.74 kun intter netissä se on välillä (0,1)

#Vähän huono jos on, koska silloin suomi toimii aika huonosti. Mutta en tiedä mikä muukaan olisi. Ehkä enkkujudgementit ei toimi
#suomelle niin hyvin.

#Pitää tutkia myös mitä suomidatasetti sanoo tän kanssa. Siis se itse tehty. Olisiko se parempi?