strs = ["flower","flow","floweght"]
# for i in strs:
    # for j in range(min(len(i) for i in strs)):
def longestCommonPrefix(strs):
    count=0
    for i in range (min(len(i) for i in strs)):
            if (all(strs[0][i]==strs[j][i] for j in range (len(strs)))) :
                count+=1
            else:
                if count==0:
                    return("")
                else:
                    return(strs[0][:count])
    if count==0:
        return("")
    else:
        return(strs[0][:count])
print(longestCommonPrefix(strs))
                

            

