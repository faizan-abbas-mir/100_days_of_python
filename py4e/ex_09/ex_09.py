#collections:dictionaries
#collecion has a key value and an order, however using key is best way to access values
cabinet= dict()
cabinet['summer']=12
cabinet['mongo']='db'
cabinet['summer']+=2
print(cabinet)
counts=dict()
print("enter line of text")
line=input()
words=line.split()
print('words:',words)
for word in words:
    counts[word]=counts.get(word,0)+1
print('count:',counts)
cunts={'joseph':1,'stephany':33,'mago':67}
for aaa,bbb in cunts.items():
    print(aaa,bbb)
