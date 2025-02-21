# #Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# # You may assume that each input would have exactly one solution, and you may not use the same element twice.
# # You can return the answer in any order.

# List=[2,4,7,14,3,5]  
# target=10

# # print(List)


# # For sorted List only
# def twoSum(List,target):
#     List.sort()
#     i=0
#     j=len(List)-1
#     while i<j:
#         if List[i]+List[j]>target:
#             j-=1
#         elif List[i]+List[j]<target:
#             i+=1
#             continue
#         else:
#             return(i,j)
# print(twoSum(List,target))
# import pandas as pd
# df1=pd.dataframe({"ID": [1,1,1,1],"Sub":["hindi","english","Math","Physics"],"Marks":[80,90,70,100]})
# df2=pd.dataframe({"ID":[1,1],"Name":{"a","a"}})

def calculate_sum_of_indices(operations):
    switches = [False] * 1000  # Initialize all switches to off
    for operation in operations:
        left, right = operation
        for i in range(left - 1, right):
            switches[i] = not switches[i]  # Toggle each switch in the interval
    total_sum = sum(i + 1 for i, switch in enumerate(switches) if switch)  # Calculate sum of indices where switch is on
    return total_sum

operations = [[1, 4], [2, 6], [1, 6]]
result = calculate_sum_of_indices(operations)
print(result)