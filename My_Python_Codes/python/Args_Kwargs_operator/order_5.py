# # PADK
# # parameter
# # args
# # default parameter
# # **kwargs
# # def function(name, *args,last_name='unknown', **kwargs):#order of input is important
# #     print(name)
# #     print(args)
# #     print(last_name)
# #     print(kwargs)
# # function('ankit',1,2,3,"Rathee",a=1,b=2,c=3) 

# # print(pow(819,216,14))
# # systemState_size = int(input())

# # systemState = list(map(int, input().split()))

# # dist_size = int(input())

# # dist = list(map(int, input().split()))

# # 2. Initialize variables to keep track of the minimum length of cable and the index of the last ON system:

# # python

# # min_cable_length = float('inf')

# # last_on_index = None

# # . Iterate through the systemState list to find the index of the last ON system:

# # python
# # def help(systemState_size,systemState,distance):
# #     for i in range(systemState_size):
# #         if systemState[i] == 1:
# #             last_on_index = i
# #     for i in range(1, last_on_index + 1):
# #         if systemState[i] == 0:
# #             cable_length = systemState[i] - systemState[last_on_index] 
# #             min_cable_length = min(min_cable_length, cable_length)




# #     print(min_cable_length)

# # help(3,[1,0,0])

#     # Here's the complete code:

#     # python

#     # systemState_size = int(input())

#     # systemState = list(map(int, input().split()))

#     # dist_size = int(input())

#     # dist = list(map(int, input().split()))

#     # min_cable_length = float('inf')

#     # last_on_index = None

#     # for i in range(systemState_size):

#     # if systemState[i] == 1:

#     # last_on_index = i




#     # python

#     # systemState_size = int(input())

#     # systemState = list(map(int, input().split()))

#     # dist_size = int(input())

#     # dist = list(map(int, input().split()))

#     # min_cable_length = float('inf')

#     # last_on_index = None

#     # for i in range(systemState_size):

#     # if systemState[i] == 1:

#     # last_on_index = i

#     # for i in range(1, last_on_index + 1):

#     # if systemState[i] == 0:

#     # cable_length = dist[i] - dist[last_on_index]

#     # min_cable_length = min(min_cable_length,

#     # cable_length)

# def min_cable_length(system_state, distances): 
#     min_cable_length = float('inf')

#     for i in range(len(system_state)):

#         if system_state[i] == 0: # If the system is OFF

#             min_distance = min(distances[i:])

#             min_cable_length = min(min_cable_length, min_distance)

#     return min_cable_length if min_cable_length != float('inf') else 0
# print(min_cable_length([1,0,1,10],[1,0,6]))
print(pow(3,44)*pow(4,55)+pow(16,6))