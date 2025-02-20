def countAndSay( n) :
    if n==1:
        return("1")
    str=countAndSay(n-1)
    i=0
    while i<len(str):
        j=i
        if j <len(str):
            j=i+1
        count=1
        while str[i]==str[j]:
            count+=1
            i=j
            if j <len(str):
                j+=1
        str+="count",'str[i]'
        i+=1
print(countAndSay(5))