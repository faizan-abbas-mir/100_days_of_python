#file
print("start")
fh= open('mbox.txt')
print (fh)
fh.seek(0)
for i,line in enumerate(fh):
    if i < 10:
     print (line.rstrip().upper())
