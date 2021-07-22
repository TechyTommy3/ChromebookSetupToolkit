print("Chromebook Setup Toolkit")
print("Alterntive Finder!")
print("Press Ctrl+C to quit at any time")
#Code is based off Search code.
#Yes, I actually mean for it to be lowercase. That is so I can make the search lowercase, and you would get the same result for eVeRYdAy use than you would for Everyday use.
searchd = {"microsoft office": "Google Docs, Sheets, and Slides", "virtualbox": "Too Intense for Chrome OS",
 "vmware workstation": "Too Intense for Chrome OS", "audacity": "Run through CrossOver",
    "playstation now": "Stadia and GeForce Now"}
while 0 == 0:
    searchterm = input("Enter a program (like Microsoft Office) to get a Chrome OS alterntive: ")
    if searchd[searchterm.lower()]:
        print(searchd[searchterm.lower()])
