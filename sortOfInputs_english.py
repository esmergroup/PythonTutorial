import time

def sortStrings():
    a = int(input("ENTER THE NUMBER OF ELEMENTS: "))
    time.sleep(0.1)

    if a>0:

        items = []

        for i in range(0, a):
            print("TYPE THE ",i,"TH ELEMENT: ")
            items.append(input())
            time.sleep(0.2)

        b = len(items)
        c = sorted(items)

        for j in range(0, b):
            print(j, " ",c[j])
            time.sleep(0.2)

        print("FINISH")
        time.sleep(0.8)

def sortNumbers():
    a = int(input("ENTER THE NUMBER OF ELEMENTS"))

    if a > 0:

        items_nr = []

        for k in range(0, a):
            print("TYPE THE ",k,"TH ELEMENT: ")
            items_nr.append(input())
            time.sleep(0.2)

        b = len(items_nr)
        c = sorted(items_nr)

        for l in range(0, b):
            print(l, " ",c[l])
            time.sleep(0.2)

        print("FINISH")
        time.sleep(0.8)

def end():
    print("")
    print("***********")
    print("PROGRAM END")
    print("***********")
    print("")
    time.sleep(0.8)
    exit()

def menue():
    while(True):
        print("")
        print("1 = SORT STRINGS")
        print("2 = SORT NUMBERS")
        print("3 = END")

        eingabe = int(input())

        if eingabe == 1:
            sortStrings()
        elif eingabe == 2:
            sortNumbers()
        elif eingabe == 3:
            end()
        else:
            print("WRONG VALUE")

print("*************")
print("PROGRAM START")
print("*************")
print("")
time.sleep(0.8)
menue()
