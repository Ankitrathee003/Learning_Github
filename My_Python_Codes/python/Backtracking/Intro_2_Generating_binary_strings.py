# given the size of binary code
output=[]
def generate_binary_str(ans,n):
    if len(ans)==n:
        output.append(ans)
        return 
    generate_binary_str(ans+[1],n)
    generate_binary_str(ans+[0],n)
generate_binary_str([],4)
print(output)


