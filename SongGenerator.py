from pymarkov import markov as m
import codecs

def formatSong(song):

	wordCount = 0
	stanzaCount = 0
	listVersion = song.split(' ')
	returnSong = ""
	for item in listVersion:
		returnSong += item
		returnSong += " "
		wordCount += 1
		if wordCount % 4 == 0:
			returnSong += "\n"
		if wordCount % 16 == 0:
			returnSong += "\n\n"

	return returnSong

f = codecs.open("newDrake2.txt",'r',"utf8")
lyrics = ""
count = 0
for line in f:
	lyrics += line[:-1].lower();
	lyrics += " "

markov_dict = m.train([lyrics],4)

print("---------------------------------------------------\n")

newSong = m.generate(markov_dict,63,4)

print(formatSong(newSong))

