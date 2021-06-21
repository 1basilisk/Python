from gtts import gTTS 
import os 
import csv
import sys
lyrics = ""

        #reads source and formats into single line
with open("source") as src:
	read =  csv.reader(src)
	for row in read:
		for char in row:
			lyrics += char
		lyrics += ", "

	    #writes formatted version into a file --- !necessary		
with open("lyrics.txt", "w") as file:
	file.write(lyrics)
	out = lyrics[:5].replace(" ", "_")

    #passes file as input.
text = lyrics

    #language as CLA, default: en
language = "en"
if len(sys.argv) == 2:
    language = sys.argv[1]

        #slow = True for slowed version.
voice = gTTS(text=text, lang=language, slow=False) 
       
        # Saving the converted audio
file = out + ".mp3" 
voice.save(file) 
  
        # Playing the audio 
os.system("mpg123 " + file)
