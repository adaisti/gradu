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
	f = open('/home/adahyvar/gradu/testidata/set2_kaannos_utf-8.tsv', 'r')
	lines = f.read()

	for line in lines.split("\n"):
		word1 = line.split("\t")[0]
		word2 = line.split("\t")[1] 
		word1 = "".join(word1.split())
		word2 = "".join(word2.split())
		print(word1, word2) 

	





if __name__ == '__main__':
	main()


