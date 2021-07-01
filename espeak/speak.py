import os

lyrics = ""
with open("source") as src:
    for row in src:
        for char in row:
            lyrics += char
        lyrics += "  "



os.system("espeak -v mb-us1 " + " \"" + lyrics + "\"")



