#Get the user directory
from pathlib import Path
home = str(Path.home())
#Make directory
#Chromebook Switching Kit
print("Chromebook Switching Kit")
#Ask for a network drive
print("Set up a network drive (on your computer or on another computer) and press enter")
#There's no press any key to continue in Python, so let's use input()
input("")
#I will stop commenting about these commands, but whenever I use print(), print("This is the text that would be shown on the screen.")
print("Now, here is some interactive help!")
input()
print("Now, plug in your Chromebook.")
input()
print("Now turn it on.")
input()
print("You can setup a network drive in the newly created folder in your Documents, or use another network drive. Please type N for the folder in your Documents, or A for another network drive.")
#Ask for an option and put it into a variable.
networkdrive = input("Make your choice now: ")
print("OK!")
if networkdrive == "A":
    networkdrivepath = input("Where is that drive located?: ")
else:
    print(home + "\\Documents\\NetworkDrive")
print("")
