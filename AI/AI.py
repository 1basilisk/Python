import os
def main():
	
		lyrics = ""
		with open("source") as src:
		    for row in src:
		        for char in row:
		            lyrics += char
		        lyrics += "  "
		
		name = input("What's your name? ")
		 
		speak("hello, " + name )
		while True:		
			human = input("talk...")
			
			if "how are you" in human:
				speak("good, what about you?")
			#		else:
			#		speak("how are you")
			
			#	human  = input("talk...")
			elif "bye" in human:
				speak("Good Bye, have a nice day")
				break
			elif "sing" in human:
				speak(lyrics)
			else:
				speak("go away")
			
def speak(this):
        #os.system("espeak -en us1 " + " \"" + this + "\"")
        os.system("espeak " + "\"" + this + "\"")
		
main()		

