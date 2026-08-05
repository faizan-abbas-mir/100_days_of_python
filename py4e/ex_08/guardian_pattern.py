hand=open("mbox.txt")

for line in hand:
    line=line.rstrip()
    """if line == "":
            continue"""
    #print(line)
    words=line.split()
    #guardian
    if len(words)<3:
        continue 
    

    if words[0] != "From":
        continue
    print(words[2])
    #strip is different from split as trip reduces to words and split reduces to words.
