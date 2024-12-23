def basic1(x):
    #for char to ascii to char
    base = ord('a')
    modified = chr(x+base)
    print(modified, end = "")

t = int(input())
while t>0:
    x = int(input())
    basic1(x)
    print()
    t =t -1