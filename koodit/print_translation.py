def translate(fif, enf, source):

	ff = open(fif)
	fi = ff.read()
	fi_w_listat = fi.split(":")

	ef = open(enf)
	en = ef.read()
	en_w_listat = en.split(":")

	
	'''
	for i in range(len(en_w)):
		print(en_w[i])
		print(fi_w[i])
	'''

	j = 0
	tulos = ""

	for line in open(source):
		words = line.split()

		if words[0] == ":":
			j = j + 1
			en_w = en_w_listat[j].split()
			fi_w = fi_w_listat[j].split()
			print(line.strip())
		else: 
			for w in words:
				t = ""
				for i in range(len(en_w)):
					if w == en_w[i]:
						t = fi_w[i].strip()
				
				#print(t, end = ' ')
				tulos += t + ' '
		if len(tulos.split()) == 4:
			print(tulos)
		tulos = ""


def main():
	p = "/Users/Ada/gradu/testidata/"
	translate(p + "analogiat_lista.txt", p + "analogiat_lista_en.txt", p + "questions_words_short.txt")

if __name__ == '__main__':
	main()