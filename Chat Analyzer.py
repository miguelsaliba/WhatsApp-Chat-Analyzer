# -*- coding: utf-8 -*-
import re

# file path to txt file
f = open("chat.txt", "r", encoding="utf8")

# skips first line which is the end to end encryption message
firstline = f.readline()

count = 0.0
people = {}
maxperday = 0
maxday = ""
currentday = ""
currentcount = 0

# removes emojis from names
def deEmojify(inputString):
    return inputString.encode('ascii', 'ignore').decode('ascii')

for x in f:
    # if the day changes it recents the day counter and checks if its more than the max day
    if (x[x.find("[")+1 : x.find(",")] != currentday):
        if currentcount > maxperday:
            maxperday = currentcount
            maxday = currentday

        currentday = x[x.find("[")+1 : x.find(",")]
        currentcount = 0

    # removes the date and time
    string = (x[x.find("]")+2:])


    # checks if its a message and not just a new line
    if re.search(".+/.+/..*:..:..", x) and ": " in string:
        # check if theres a new person
        if (string.split(": ")[0] not in people):
            people[string.split(": ", 1)[0]] = 0

        # adds message to person
        people[string.split(": ")[0]] += 1


        count += 1
        # counter for one day
        currentcount += 1

print("Total: {0:,g}".format(count))
print("Most messages per day: {:,} - {}".format(maxperday, maxday))

for i, j in sorted(people.items(), key=lambda x:x[1], reverse=True):
    print("{}: {:,g} - {:0.2f}%".format(deEmojify(i), j, j/count*100))
