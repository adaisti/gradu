#!/usr/bin/env python
# -*- coding: utf-8 -*-





#1. tee funktio, joka hakee listan sukulaissanoista ontologiasta
#2. sellainen, joka hakee saman fasttextistä
#3. funktio, joka vertaa 1. ja 2. tuloksia
#4. koodaa silmukka, jossa vaihdetaan fasttextin parametreja
#2. pitäisi mennä näin:
#subprocess.check_output("fasttextkomento").split("\n").split(" ")

import urllib3
import json
import subprocess


def related(word):
	http = urllib3.PoolManager()
	r = http.request('GET', 'http://api.finto.fi/rest/v1/search?query=' + word + '&lang=fi&labellang=fi&vocab=yso&fields=related%20narrower')
	data = json.loads(r.data.decode('utf-8'))

	#print(data)
	results = []


	if len(data["results"]) == 0:
		return results

	for x in data["results"][0]["skos:related"]:
		y = x["prefLabel"]
		results.append(y)

	return results

def main():

	words = ["hulluruoho", "poikaystävät", "kana", "tyttöystävät", "hevonen"]

	for word in words:
		orig = word
		word = word.replace('ä', '%C3%A4')
		word = word.replace('ö', '%C3%B6')

		print(orig + ": ")
		print(related(word))

	#result = subprocess.check_output(["./fasttext",  "nn",  "result2/fil9.bin"])
	#print(result)



if __name__ == '__main__':
	main()

