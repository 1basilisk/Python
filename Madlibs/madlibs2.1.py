"""
prints and saves madlibs
"""

import datetime

print("				Madlibs Maker")


name  = input("Enter your name:	");

var1= input("Type a name:   ")
var2 = input("Type a wacky state:    ")
var3 = input("Type a verb :    ")
var4= input("Type a noun :    ")
v5 = input("Type a female name :    ")
v6= input("Type a verb :    ")
v7 = input("Type a noun :    ")
v8 = input("Type a verb :    ")
v9 = input("Type a noun :    ")
v10 = input("Type a part of body:    ")
v11 = input("Type an adjective:    ")
v12 = input("Type a relative :    ")
v13 = input("Type a running activity :    ")
v14= input("Type a chain restraunt:    ")
v15 = input("Type a verb(past form):    ")
v16 = input("Type a month:    ")
v17 = input("Type a verb in +ing form :    ")
v18 = input("Type a noun :    ")
v19 = input("Type a verb in past :    ")
v20 = input("Type an adjective:    ")
v21 = input("Type a verb :    ")
v22 = input("Type a thing :    ")
v23 = input("Type a plural noun :    ")
#verb1 = input("Type a verb :    ")
#verb1 = input("Type a verb :    ")
#verb1 = input("Type a verb :    ")

#saves to;file;
file = open("story.txt", "a")
current_time = datetime.datetime.now()
file.write("\nName: " + name + "\nTime: " + str(current_time) + ".\n")

file.write(var1 + " in " + var2 + " state was arrested this morning after he " + var3 + " in front of " + var4 + ". " + var1 + ", had a history of " + v6 + ", but no-one, not even his " + v7 +" ever imagined he'd " + v8 +" with a " + v9 + " stuck in his " + v10 + ".\n")

file.write("\" I always thought he was " + v11 + ", but I  never thought he'd do something like this. Even his " + v12 + " was surprised\"\n")

file.write("After a brief " + v13 + ", cops followed him to a " + v14 + ", where he reportedly " + v15+ " in the fry machine.\n")

file.write("In " +v16+ ", a woman "  +  v5 + " was charged with a similar crime. But rather than " +v17+ " with a " + v18 + ", she " + v19 + " with a " + v20 + " dog.\n")

file.write("Either way, we imagine that after witnessing him " + v21 + " with a " + v22 + " there are probably a whole lot of " + v23 + " that are going to need some therapy\n\n\n")

#print;on screen
print(var1 + " in " + var2 + " state was arrested this morning after he " + var3 + " in front of " + var4 + ". " + var1 + ", had a history of " + v6 + ", but no-one, not even his " + v7 +" ever imagined he'd " + v8 +" with a " + v9 + " stuck in his " + v10 + ".\n")

print("\" I always thought he was " + v11 + ", but I  never thought he'd do something like this. Even his " + v12 + " was surprised\"\n")

print("After a brief " + v13 + ", cops followed him to a " + v14 + ", where he reportedly " + v15+ " in the fry machine.\n")

print("In " +v16+ ", a woman "  +  v5 + " was charged with a similar crime. But rather than " +v17+ " with a " + v18 + ", she " + v19 + " with a " + v20 + " dog.\n")

print("Either way, we imagine that after witnessing him " + v21 + " with a " + v22 + " there are probably a whole lot of " + v23 + " that are going to need some therapy\n\n\n")

file.close()