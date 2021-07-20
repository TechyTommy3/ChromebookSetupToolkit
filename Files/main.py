#Get the user directory
from pathlib import Path
home = str(Path.home())
#Import the browser module
import webbrowser as browser
#Make directory
#Chromebook Switching Kit
print("Chromebook Switching Kit")
#Ask for Google Drive and open it's website
print("Chromebook Setup Toolkit requires Google Drive for Desktop.")
input()
browser.open("https://support.google.com/drive/answer/7329379")
print("Install Google Drive for Desktop and press enter")
#There's no press any key to continue in Python, so let's use input()
input("")
#I will stop commenting about these commands, but whenever I use print(), print("This is the text that would be shown on the screen.")
print("Now, here is some interactive help!")
input()
print("Now, plug in your Chromebook.")
input()
print("Now turn it on.")
input()
print("Now set it up with the account!")
input()
#Ask for an option and put it into a variable.
networkdrive = input("Please type what drive you have Google Drive for Desktop configrued on.")
print("OK!")
