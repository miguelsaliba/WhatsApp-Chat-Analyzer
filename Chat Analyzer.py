# -*- coding: utf-8 -*-
import re

f = open("chat.txt", "r", encoding="utf8")
firstline = f.readline()

count = 0.0
people = {}
maxperday = 0
maxday = ""
currentday = ""
currentcount = 0

def deEmojify(inputString):
    return inputString.encode('ascii', 'ignore').decode('ascii')

for x in f:
    if (x[x.find("[")+1 : x.find(",")] != currentday):
        if currentcount > maxperday:
            maxperday = currentcount
            maxday = currentday

        currentday = x[x.find("[")+1 : x.find(",")]
        currentcount = 0

    string = (x[x.find("]")+2:])


    if re.search(".+/.+/..*:..:..", x) and ": " in string:
        if (string.split(": ")[0] not in people):
            people[string.split(": ", 1)[0]] = 0

        people[string.split(": ")[0]] += 1


        count += 1
        currentcount += 1

print("Total: {0:,g}".format(count))
print("Most messages per day: {:,} - {}".format(maxperday, maxday))

for i, j in sorted(people.items(), key=lambda x:x[1], reverse=True):
    print("{}: {:,g} - {:0.2f}%".format(deEmojify(i), j, j/count*100))
