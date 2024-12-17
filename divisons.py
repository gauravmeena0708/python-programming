def counting_digits():
    # printing the digits and counting the number of digits
    number = 12735
    num = 10
    cnt = 0
    while number>0:
        print(number%10, end=" ")
        cnt = cnt + 1
        number = number // num
    print("count->",cnt)

def reversing_number():
    #reversing the number
    number = 127300
    num = 10
    cnt = 0
    rev = 0
    while number>0:
        rem = number%10
        rev = 10*rev+rem
        cnt = cnt + 1
        number = number // num
    print("count->",cnt)
    print(rev)

def checking_palindrome():
    #checking palindrome
    number = 1331
    dup = number
    num = 10
    cnt = 0
    rev = 0
    while number>0:
        rem = number%10
        rev = 10*rev+rem
        cnt = cnt + 1
        number = number // num
    if(dup == rev):
        print("Yes")
    else:
        print("No")

def checking_armstrong():
    # Checking Armstrong number
    number = 1634
    dup = number
    num_digits = len(str(number))
    sum = 0
    while number > 0:
        digit = number % 10
        number = number // 10
        sum += digit ** num_digits
    if dup == sum:
        print("Yes")
    else:
        print("No")

def divisors(x):
    #finding divisors
    for i in range(1, round(x**0.5+1), 1):
        if x%i==0:
            print(i, end = " ")
            if i != x//i:
                print(x//i, end=" ")

def check_prime(x):
    # Check if x is prime
    is_prime = True
    if x <= 1:
        is_prime = False
    else:
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                is_prime = False
                break
    print(is_prime)

def find_gcd(x):
    #find gcd
    num1, num2 = 24, 40
    gcd = 0
    for i in range(min(num1, num2),1,-1):
        if num1%i==0 and num2%i==0:
            gcd = i
            break
    print(gcd, end="")

def find_gcd2(x):
    #gcd(n1,n2) = gcd(n1-n2, n2)
    #gcd(n1, n2) = gcd(n1%n2)
    def gcd(n1, n2):
        if n2>n1:
            n1, n2 = n2, n1
        if n1==0:
            return n2
        elif n2==0:
            return n1
        else:
            return gcd(n1%n2,n2)
    num1, num2 = 24, 40
    print(gcd(num1,num2), end="")    

def find_gcd3(x):
    def gcd(a,b):
        while a and b:
            if a>b:
                a=a%b
            else:
                b=b%a
        return max(a,b)
    print(gcd(51,17), end="")

t = int(input())
while t>0:
    x = int(input())
    find_gcd2(x)
    print()
    t =t -1

