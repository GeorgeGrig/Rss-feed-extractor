import os

#Opens target file and splits all the urls

file = "subscription_manager"
readfile = open(file, "r",encoding="utf8")

target = readfile.read()
i = 1
y = 1
while True:
    try:
        target = target.split('xmlUrl="',1)
        result = target[1].split('" />',1)[0]
        print (result)
        target = target[1].split('" />',1)[1]
        i += 1
        if i>99:
            i = 1
            print ("Part "+ str(y) + " ################################################################################################### " + "Part "+ str(y))
            y += 1
    except:
        print ("done,I guess")
        break

