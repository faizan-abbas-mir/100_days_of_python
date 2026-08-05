#lists
# concatinate 
"""list1= ["apple", "banana"]
list2= [1,2.3,4,5]

list3=list1+list2
print(list3)
print( min(list2))   #built in fn

stuff = list()

stuff.append("book")
stuff.append("mango")
stuff.append("APPLE")
stuff.sort()

print(stuff)
if "boosk" in stuff:
    print("got it")
else: 
    print("nope")"""


"""
num_list=[]
new_num=""
while True:
    new_num=(input("enter new number:"))
    if new_num=="done":
        break
    else:
        num_list.append(int(new_num))
print(num_list)
total=sum(num_list)
count=len(num_list)
average=total/count
print(average)

asty =[1,2,3,4,5]
print(asty[1:3])
"""
"""x=[]                        #constructor method
print(type(x))
#print(dir(x))
x.append("mango")
#cannot concatinat a string to list using + 
print(x)
if "mango" not in x:
    print("gugu")
else:
    print("gaga")"""
sentence =" this is a string to be split"
listed=sentence.split()
print(listed)
print(len(listed))
for w in sentence:
    print(w)
for d in listed:
    print(d)

tricky="split;on;terminator"
splitedterminator=tricky.split(";")
print(splitedterminator)


fhand=open("test.txt")
word_list=[]
for indivisual in fhand:
    word_list=indivisual.split()
    if "From" not in word_list:
        print("nf")
        continue
    print(word_list[2])
    email=word_list[1]
    splitted_email=email.split("@")
    print("sendername : "+splitted_email[0])
    print("domain : "+ splitted_email[1])