s='(a,b,w)'

def isValid(s):
    l=[]
    for i in s:
        if i =="(" or i== "[" or i== "{":
            l.append(i)

        else:
            if i ==')':
                if l and l[-1]=='(':
                    l.pop()
                else:
                    return(False)

            if i == '}':
                if l and l[-1]=='{':
                    l.pop()
                else:
                    return(False)

            if i ==']':
                if l and l[-1]=='[':
                    l.pop()
                else:
                    return(False)


    return(l==[])

print(isValid(s))