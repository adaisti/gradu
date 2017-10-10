#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main():
	f = open('/Users/Ada/gradu/testidata/fiwn-lexrels.tsv', 'r')

	lines = f.read()

	for line in lines.split("\n"):
		word1 = line.split("\t")[1]
		word2 = line.split("\t")[3]
		relation = line.split("\t")[5]




if __name__ == '__main__':
	main()