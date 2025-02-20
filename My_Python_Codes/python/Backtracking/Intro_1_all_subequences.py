# Printing all subequences of an list
# Initialize lists to store subsequences and the current subsequence being formed.
ans = []
output = []
# Define a function to generate all subsequences of a list 'l'.
def allSubsequences(l, ans):
    # Base case: If the input list 'l' is empty, append the current 'ans' to 'output'.
    if len(l) == 0:
        output.append(ans)
        return
    # Recursive case:
    # 1. Include the first element of 'l' in the current subsequence and recurse.
    allSubsequences(l[1:], ans+[l[0]])
    # 2. Exclude the first element of 'l' from the current subsequence and recurse.
    allSubsequences(l[1:], ans)
    return 

# Call the 'allSubsequences' function with an initial empty 'ans' and store the result.
arr=[1, 2, 3]
allSubsequences(arr, ans)
print(output)









# def generate_subsequences(text, dictionary, i, current_subsequence):







