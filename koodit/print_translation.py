def translate(fif, enf, source):

	f = open(fif)
	fi = f.read()
	fi_w = fi.split("")

	e = open(enf)
	en = e.read()
	en_w = en.split("")
	
	for line in open(source):
		
		
		


def main():
	p = "Users/Ada/gradu/testidata/"
	translate(p + "analogiat_lista.txt", p + "analogiat_lista_en.txt", p + "questions_words.txt")

if __name__ == '__main__':
	main()