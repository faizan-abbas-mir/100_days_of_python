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