#Get the user directory
from pathlib import Path
#Import some libraries that allow us to copy in Python
import shutil, os
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
print("Now, here is some help!")
input()
print("Now, plug in your Chromebook.")
input()
print("Now turn it on.")
input()
print("Now set it up with the account you use on here!")
input()
print("Welcome to Chromebook!")
input()
print("Now, if you don't use Chrome, please switch to Chrome using the same account you use on your Chromebook.")
networkdrive = input("Please type what drive you have Google Drive for Desktop configrued on.")
print("OK!")
print("Now let's check alterntives.")
print("When done, type in done.")
exec(open("alterntive.py").read())
print("Now in copying mode.")
print("Copying mode copies files, but saves space by not transferring files that Chromebooks can't use. (Not working right now)")
while 0 == 0:
    files = input("Please type a folder to copy to Google Drive.")
    shutil.copytree(files, networkdrive + ':\\SetupToolkit')
