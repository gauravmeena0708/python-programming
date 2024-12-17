def match_brackets(s):
    #finding redundant bracket
    #go character by character -> if ) -> pop till ( however check if this sequence contains +-*/
    #                             else append the char
    s = "(a+((b+c)))"
    stack = []
    for char in s:
        print(stack)
        if char == ')':
            top = stack.pop()
            has_operator = False
            while top != '(':
                if top in '+-*/':
                    has_operator = True
                top = stack.pop()
            if not has_operator:
                return True
        else:
            stack.append(char)
    
    return False

t = int(input())
while t>0:
    x = int(input())
    match_brackets(x)
    print()
    t =t -1