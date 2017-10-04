#!/usr/bin/env python
# -*- coding: utf-8 -*-



import subprocess
from scipy.spatial.distance import cosine
from scipy.stats import spearmanr
import numpy as np
from bokeh.plotting import figure, output_file, show


def print_words():
	f = open('/home/adahyvar/gradu/testidata/combined.tab', 'r')
	lines = f.read()
	
	for line in lines.split("\n"):
		word1 = line.split("\t")[0]
		word2 = line.split("\t")[1]
		print(word1)
		print(word2)

def main():



	#print_words()
	#return



	#	word1 = "".join(word1.split())
	#	word2 = "".join(word2.split())
	#	print(word1, word2) 

	output_file("lines.html")

	#f = open('/home/adahyvar/gradu/testidata/set2_vectors.txt', 'r')
	f = open('/home/adahyvar/gradu/testidata/combined_vectors.txt', 'r')
	lines = f.read()

	vectors = []

	for line in lines.split("\n"):
		vector = np.array(line.split()[1:], dtype=float)
		vectors.append(vector)



	scores = []

	words = []

	#f2 = open('/home/adahyvar/gradu/testidata/set2_kaannos_utf-8.tsv', 'r')
	f2 = open('/home/adahyvar/gradu/testidata/combined.tab', 'r')
	
	lines2 = f2.read()

	for line in lines2.split("\n"):



		score = line.split("\t")[2]
		scores.append(score)
		word1 = line.split("\t")[0]
		word2 = line.split("\t")[1] 
		words.append(word1 + " " + word2)

	similarities = []

	for i in range(0,len(vectors) - 2,2):
		similarities.append(1 - cosine(vectors[i], vectors[i + 1]))

	similarities = similarities[1:]	#1 koska eka rivi on sellainen turha
	scores = scores[1:]#
	words = words[1:]

	#print(len(similarities), len(scores), len(words))
	#return

	#for i in range(0, len(similarities)):	
		#print(words[i], similarities[i], scores[i])

	scores = np.array(scores)
	similarities = np.array(similarities)
	p = figure(title="simple line example", x_axis_label='x', y_axis_label='y')
	p.line(similarities, scores, legend="Temp.", line_width=2)

	show(p)






		





	

	





if __name__ == '__main__':
	main()