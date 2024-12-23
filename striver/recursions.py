def rec1(x):
    #simple recursion
    def rec(i,x):
        if i<1:
            return
        print(i, end="")
        rec(i-1,x)
    rec(x,x)

def rec2(x):
    #simple recursion reversed
    def rec(i,x):
        if i<1:
            return
        rec(i-1,x)
        print(i, end="")
    rec(x,x)

def rec3(x):
    def backtrack(i, x):
        if i > x:
            return
        backtrack(i+1, x)
        print(i, end="")
    backtrack(1, 5)

def rec4(x):
    def recsum(n):
        if n<=1:
            return 1
        return n+recsum(n-1)
        
    print(recsum(x), end="")

def rec5(x):
    def recfact(n):
        if n<=1:
            return 1
        return n*recfact(n-1)
        
    print(recfact(x), end="")

def rec6(x):
    #reverse string using recursion,... convert string to list as string can not be replaced using indices
    a = list("hello")
    
    def reverse(l, r):
        if l >= r:
            return
        a[l], a[r] = a[r], a[l]
        reverse(l + 1, r - 1)
    
    reverse(0, len(a) - 1)
    print("".join(a), end="")

def rec7(x):
    s = "11232211"
    #check pelindrome 
    n = len(s)
    def rec_palindrome(i):
        if i>=n/2:
            return True
        else:
            if s[i] != s[n-i-1]:
                return False
            else:
                return rec_palindrome(i+1)
    print(rec_palindrome(0), end="") 


def rec8(x):
    def rec_fibo(n):
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            return rec_fibo(n - 1) + rec_fibo(n - 2)
    print(rec_fibo(x), end="")

def rec9(x):
    #tower of hanoi
    # if n=1, move source to destination
    # if n>=1 move n-1 from source to auxillary using recursive approach (if t3 is auxillary)
    # -> first move d1 to t2, d2 to t3 > move d2 to t3 
    # move d3 to t2 and move d1 to t1, d2 to t2 and d1 to t2 ()
    # lets say 3 - using above steps tower  
    # recursive algo if n = 1 move source to dest else move n-1 to aux, move last to dest, move aux to dest 

    moves = []

    
    def solve(n, source, destination, auxiliary):
        if n == 1:
            moves.append([source, destination])
        else:
            solve(n - 1, source, auxiliary, destination)
            moves.append([source, destination])
            solve(n - 1, auxiliary, destination, source)


    solve(x, 1, 3, 2)
    print(len(moves), end="")

def fibonacci(n, memo={}):
    if n <= 1:
        return n
    
    if n in memo:
        return memo[n]
    
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    
    return memo[n]


n = 10
print(f"Fibonacci of {n} is: {fibonacci(n)}")

### GP with modulo so that the number does not overflow
"""
import sys
from sys import stdin

MOD = 10**9 + 7

def mod_exp(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

def nthTermOfGP(N, A, R):
    if N == 1:
        return A % MOD
    

    R_power = mod_exp(R, N - 1, MOD)
    result = (A * R_power) % MOD
    return result

t = int(sys.stdin.readline().strip())

while(t > 0):
    
    n, a, r = map(int,input().split())
    print(nthTermOfGP(n,a,r))
    
    t = t - 1
"""
#essential steps for recursive problem
# show that it works for n ==1
#assume f(n-1) works 
#show that f(n) works if f(n-1) worked
#example stack of domino -> if you knock 1 domino it will fall, if f(n-1) domino falls f(n) will also fall
t = int(input())
while t>0:
    x = int(input())
    rec9(x)
    print()
    t =t -1
