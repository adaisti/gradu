#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sklearn.manifold import TSNE
import numpy as np


def main():
	

	f = open('/home/adahyvar/gradu/testidata/visu_vektorit.txt', 'r')
	lines = f.read()

	vectors = []
	words = []

	for line in lines.split("\n"):

		if line == "":
			continue

		l = line.split()[1:]
		words.append(line.split()[0])

		vector = np.array(l, dtype=float)

		if len(vector) == 0:
			continue

		vectors.append(vector)

	vecs = np.array(vectors)
	#print(vecs.shape)

	vectors_embedded = TSNE(n_components=3).fit_transform(vecs)
	#print(vectors_embedded.shape)


	print("window.xcords=[", end ='')


	for i in range(len(vectors_embedded) - 1):
		print(vectors_embedded[i][0], end ='')
		print(', ', end ='')

	print(vectors_embedded[-1][0], end ='')
	print(']')

	print("window.ycords=[", end ='')


	for i in range(len(vectors_embedded) - 1):
		print(vectors_embedded[i][1], end ='')
		print(', ', end ='')

	print(vectors_embedded[-1][1], end ='')
	print(']')

	print("window.zcords=[", end ='')


	for i in range(len(vectors_embedded) - 1):
		print(vectors_embedded[i][2], end ='')
		print(', ', end ='')

	print(vectors_embedded[-1][2], end ='')
	print(']')


	print('window.names=["', end ='')


	for i in range(len(vectors_embedded) - 1):
		print(words[i], end ='')
		print('", "', end ='')

	print(words[-1], end ='')
	print('"]')
	


if __name__ == '__main__':
	main()