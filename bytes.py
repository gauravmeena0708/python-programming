def task11(x):
    s = "0011100"
    #checking distance from alternating 0101 or 1010 string
    count1 = 0
    count2 = 0
    
    for i in range(len(s)):
        bit1 = i % 2
        bit2 = 1 - bit1
        
        if int(s[i]) != bit1:
            count1 += 1
        if int(s[i]) != bit2:
            count2 += 1
    print(min(count1, count2), end="")