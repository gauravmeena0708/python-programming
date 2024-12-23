def pattern_01(x, y):
    for i in range(x):
        for j in range(y):
            print("*", end=" ")
        print()

def pattern_02(x):
    for i in range(x):
        for j in range(i+1):
            print("*", end=" ")
        print()

def pattern_03(x):
    for i in range(x):
        for j in range(i+1):
            print(str(j+1)+" ", end=" ")
        print()

def pattern_04(x):
    for i in range(x):
        for j in range(i+1):
            print(str(i+1)+" ", end=" ")
        print()

def pattern_05(x):
    for i in range(x):
        for j in range(x-i):
            print(str("*")+" ", end=" ")
        print()

def pattern_06(x):
    for i in range(x):
        print(" "*(x-i-1) + "*"*(2*(i+1)-1), end=" ")
        print()

def pattern_07(x):
    for i in range(x):
        print(" "*(i) + "*"*(2*x-2*(i)-1), end=" ")
        print()



def pattern_08(x):
    for i in range(2*x-1):
        if i<=x-1:
            print("*"*(i+1), end=" ")
        else:
            print("*"*(2*x-i-1), end=" ")
        print()

def pattern_09(x):
    start = 0
    for i in range(2*x-1):
        lim = 0
        if i<=x-1:
            lim = i+1
        else:
            lim = 2*x-i-1

        if i %2 == 0:
            start = 0
        else:
            start = 1
        for j in range(lim):
            
            print(start, end=" ")
            if start == 0:
                start = 1
            else:
                start = 0
            
        print()

def pattern_10(x):
    for i in range(x):
        for j in range(i+1):
            print(j+1, end=" ")
        for j in range(2*x-2*i-2):
            print(" ", end=" ")
        for j in range(i+1):
            print(i-j+1, end=" ")
        print()



def pattern_11(n):
    for i in range(n):
        print(" "*(n-i-1)+"*"*(2*i+1))

def pattern_12(n):
    for i in range(0, 2*n, 1):
        #print(i)
        if i<n:
            for j in range(n-i):
                print("*", end="")
            for j in range(2*i):
                print(" ", end="")
            for j in range(n-i):
                print("*", end="")
        else:
            for j in range(i-n+1, 0, -1):
                print("*", end="")
            for j in range(2*(2*n-i-1)):
                print(" ", end="")
            for j in range(i-n+1, 0, -1):
                print("*", end="")
        print()

def pattern_13(n):
    for i in range(n):
        if i==0 or i == n-1:
            print("*"*n)
        else:
            print("*"+" "*(n-2)+"*")

def pattern_14(n):
    for i in range(n):
        for j in range(n):
            if i==0 or i == n-1 or j==0 or j==n-1:
                print("*", end = "")
            else:
                print(" ", end = "")
        print()

#distance from the center = n - min of (distance from top, bottom, left, right)
#distance from the center = n - min of (j, size-j, i, size-i)
def pattern_15(n):
    size = 2 * n -1
    for i in range(size):
        for j in range(size):
            # Calculate the number to print based on the minimum distance to the edge
            k = min(i, j, size - i - 1, size - j - 1)
            print(n-k-1, end="")
        print()

def switch_case(option, i, j, size, n):
    if option == 1:
        if j<=i and i<n and j<n:
            print(0, end="")
    elif option == 2:
        if j<=i and i<n and j<n:
            print(i, end="")
    elif option == 3:
        if j<=i and i<n and j<n:
            print(j+1, end="")
    elif option == 4:
        if j<=i and i<n and j<n:
            print(n-j, end="")
    elif option == 5:
        if j<=i and i<n and j<n:
            print(n-i, end="")
    elif option == 6:
        if j<=i and i<n and j<n:
            print(abs(i-j), end="")
    elif option == 7:
        if i<n and (i>=j or j+i+1>=2*n):
            print(0, end="")
        elif i<n:
            print(" ", end="")
    elif option == 8:
        if i<n and (i>=j or j+i+1>=2*n):
            print(j, end="")
        elif i>=n and (j>=i or (j<=2*n-i-1)):
            print(j, end="")
        else:
            print(" ", end="")
        
    
    elif option == 998:
        if j<=i and i<n and j<n:
            k = min(i, j, size-i-1)
            print(k, end="")
        else:
            print("", end="")
    elif option == 999:
        if i<=j and i<n and j<n:
            k = min(i, j, size-i-1)
            print(n-k, end="")
        else:
            print("", end="")
    else:
        print("Invalid option")




def pattern_switch(n):
    size = 2*n
    for i in range(size):
        for j in range(size):
            switch_case(8, i, j, size, n)        
        print()

t = int(input())
while t>0:
    x = int(input())
    pattern_12(x)
    print()
    t =t -1