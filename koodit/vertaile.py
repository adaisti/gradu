#!/usr/bin/env python
# -*- coding: utf-8 -*-



#ajo-ohje
#ensin print_wordsillä sanat omilla riveillään tiedostoon
#sitten siitä tiedostosta vektoritiedosto fasttextin print-word-vectorsilla  _vectors -tiedostoon
#ja siitä sitten loppuosalla tätä koodia vertailut


# tuloksia

# itse opetettu enkku: 
# rw: SpearmanrResult(correlation=0.39995046504647752, pvalue=5.9064952459193522e-79)
# ws353: SpearmanrResult(correlation=0.61896880486607464, pvalue=1.0358009632396432e-38)

# netistä ladattu enkku:
# rw: SpearmanrResult(correlation=0.45743263313679539, pvalue=1.1186986601267153e-105)
# ws353: SpearmanrResult(correlation=0.6677145487051418, pvalue=6.4635265180046649e-47)

# paperin mukaan:
# rw: 47
# ws353: 71



import subprocess
from scipy.spatial.distance import cosine
from scipy.stats import spearmanr
import numpy as np



def print_words():
	#f = open('/home/adahyvar/gradu/testidata/combined.tab', 'r')
	f = open('/home/adahyvar/gradu/testidata/rw.txt', 'r')
	#f = open('/Users/Ada/gradu/testidata/combined.tab', 'r')

	#f = open('/Users/Ada/gradu/testidata/suomi1.tsv', 'r')

	lines = f.read()
	
	for line in lines.split("\n"):
		if line == "":
			continue
		word1 = line.split("\t")[0]
		word2 = line.split("\t")[1]
		print(word1)
		print(word2)


def similarities_words(lines2, vectors):

	words = []

	for line in lines2.split("\n"):
		if line == "":
			continue

		word1 = line.split("\t")[0]
		word2 = line.split("\t")[1] 
		words.append(word1 + " " + word2)

	similarities = []

	for i in range(0,len(vectors) - 2,2):
		similarities.append(1 - cosine(vectors[i], vectors[i + 1]))

	similarities = similarities[1:]	#1 koska eka rivi on sellainen turha
	words = words[1:]

	#return similarities, words
	for i in range(len(similarities)):
		print(words[i], similarities[i])


def main():



	#print_words()
	#return



	#	word1 = "".join(word1.split())
	#	word2 = "".join(word2.split())
	#	print(word1, word2) 

	#f = open('/home/adahyvar/gradu/testidata/set2_vectors.txt', 'r')
	f = open('/home/adahyvar/gradu/testidata/combined_vectors.txt', 'r')
	#f = open('/home/adahyvar/gradu/testidata/rw_vectors.txt', 'r')	#tai mikä tiedostonimeksi tuleekaan
	
	#f = open('/Users/Ada/gradu/testidata/combined_vectors.txt', 'r')
	#f = open('/Users/Ada/gradu/testidata/set2_suomi_vektorit.txt', 'r')
	#f = open('/Users/Ada/gradu/testidata/combined_vectors.txt', 'r')
	
	

	lines = f.read()

	vectors = []

	for line in lines.split("\n"):
		vector = np.array(line.split()[1:], dtype=float)
		vectors.append(vector)



	scores = []


	#f2 = open('/home/adahyvar/gradu/testidata/set2_kaannos_utf-8.tsv', 'r')
	f2 = open('/home/adahyvar/gradu/testidata/combined.tab', 'r')
	#f2 = open('/home/adahyvar/gradu/testidata/rw.txt', 'r')
	
	#f2 = open('/Users/Ada/gradu/testidata/combined.tab', 'r')
	#f2 = open('/Users/Ada/gradu/testidata/suomi1.tsv', 'r')
	#f2 = open('/Users/Ada/gradu/testidata/set2_kaannos_utf-8.tsv', 'r')


	lines2 = f2.read()

	#similarities_words(lines2, vectors)

	#return

	words = []



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

	similarities = []

	for i in range(0,len(vectors) - 2,2):
		similarities.append(1 - cosine(vectors[i], vectors[i + 1]))

	similarities = similarities[1:]	#1 koska eka rivi on sellainen turha
	scores = scores[1:]#
	words = words[1:]

	#print(len(similarities), len(scores), len(words))
	#return

	for i in range(0, len(similarities)):	
		#print(words[i], similarities[i], scores[i])

		d = 0.2


		#if float(scores[i])/10 < similarities[i] + d and float(scores[i])/10 > similarities[i] - d:
		#	print(words[i], similarities[i], scores[i])


		if not (float(scores[i])/10 < similarities[i] + d and float(scores[i])/10 > similarities[i] - d):
			print(words[i], similarities[i], scores[i])
	scores = np.array(scores)

	#np.isfinite(similarities).any()
	#np.isfinite(np.sum(scores))

	print(spearmanr(similarities, scores))






		





	

	





if __name__ == '__main__':
	main()