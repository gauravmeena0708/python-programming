def task1(x):
    if 'dct' not in locals():
        arr = [5,3, 4 , 1 , 7,  8, 5, 3, 2, 1]
        dct = {}
        for i in arr:
            if i in dct:
                dct[i] += 1
            else:
                dct[i] = 1
    print(dct[x], end="")

t = int(input())
while t>0:
    x = int(input())
    task1(x)
    print()
    t =t -1
