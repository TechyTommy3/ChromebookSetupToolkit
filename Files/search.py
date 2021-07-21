print("Chromebook Setup Toolkit")
print("Chromebook Finder!")
print("Press Ctrl+C to quit at any time")
#Yes, I actually mean for it to be lowercase. That is so I can make the search lowercase, and you would get the same result for eVeRYdAy use than you would for Everyday use.
searchd = {"single device": "Lenovo Chromebook Duet", "everyday use": "Google Pixelbook Go",
"on a budget": "Lenovo Chromebook Duet", "tablet mode coding": "Google Pixelbook",
  "virtual machines on a chromebook": "Google Pixelbook Go", "all day travel": "Google Pixelbook Go",
    }
while 0 == 0:
    print("To print out all possible search terms, run this through IDLE, press Ctrl+C, and type in searchd.")
    searchterm = input("Enter a task to find the best Chromebook for it.")
    if searchd[searchterm.lower()]:
        print(searchd[searchterm.lower()])
