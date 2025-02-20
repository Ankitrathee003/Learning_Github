a={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

s="ID"

output=0
if len(s)==1:
    output=a[s]
else:    
    for i in range(len(s)-1):
        if a[s[i]]>=a[s[i+1]]:
            output+=a[s[i]]
            if i+1==len(s)-1:
                    output+=a[s[i+1]]
        else:
            output-=a[s[i]]
            if i+1==len(s)-1:
                    output+=a[s[i+1]]
print(output)
