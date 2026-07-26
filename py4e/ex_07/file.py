#file
fname=input("enter file name:")
try:
    fhand=open(fname)
    count=0
    fhand.seek(0)
    inpt = fhand.read()
    print(inpt[:2])
    fhand.seek(0)
    for cheese in fhand:
        count+=1
        print(cheese.rstrip())
        if cheese.startswith("hello"):
            print(f"line matches:{cheese}")

    print(f"line count= {count}")

except:
    print("what is this name you idiot!!!f")
