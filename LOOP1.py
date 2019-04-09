print("[OUR FIRST LOOP IS THE FOR LOOP]")

for i in range(0, 11, 1):
    if(i%2==0):
        print(i, "\t [is Straight number]")
    elif(i%2 != 0):
        print(i,"\t [is odd number]")


print("[OUR SECOUND LOOP IS THE WHILE LOOP]")

a = 10
b = 0

while(a <= 10):
    print(a)
    a -= 1
    if(a==0):
        print("\t [A IS NOW FINISHED]")
        break

while(b >= 0):
    print(b)
    b += 1
    if(b== 10):
        print("\t [B IS NOW FINISHED]")
        break
