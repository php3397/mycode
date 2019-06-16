import sys

def r_file(filename):
	print(filename)
	all_words = []
	print(all_words)
	with open(filename,'r') as f:
		for lines in f.readlines:
			words_inline = lines.split()
		print(words_inline)
			for word in words_inline:
				all_words.append(word)

print("below is all words",all_words)


r_file(sys.argv[1])

