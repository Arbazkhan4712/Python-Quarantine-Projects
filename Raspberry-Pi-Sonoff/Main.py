from time import sleep

a = int(input("Enter Time"))
a = a*60
t = 1
while True:
    print(t)
    t = t+1
    if t == a:
        print("Done")
        exit()
    sleep(1)