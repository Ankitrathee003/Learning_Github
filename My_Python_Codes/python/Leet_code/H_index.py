def hIndex(citations) :
    if len(citations)>1:
    # finding max
        max=citations[0]
        i=0
        while i < len(citations):
            if max>citations[i]:
                i+=1
            else:
                max=citations[i]
                i+=1
            print(max)
        if max==0:
            return(0)
        count_array=[0]*(max+1)
        for i in citations:
            count_array[i]+=1
            
        count=0
        for i in range (-1,-(max+1),-1):
                count+=count_array[i]
                count_array[i]=count
        print(count_array)
        j=-1
        while j>-(max+1):
            if  count_array[j]>=(max+1+j):
                return(max+1+j)
            else:
                j-=1
    else:
            return(min(1,citations[0]))  

l=[11,15]

print(hIndex(l))