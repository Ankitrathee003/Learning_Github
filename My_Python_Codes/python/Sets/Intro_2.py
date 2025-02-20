#in keyword

# s={'a','b','c','d'}
# if 'a' in s:
#     print("Present")
# else:
#     print("Absent")


#unordered collection
# for i in s:   #unordered collection so can come in any order
#     print(i)


#Union  #intersection
s1={1,2,3,3,4,5}
s2={4,5,6,7,7,8}

union_set=(s1|s2)
print(union_set)

intersection=(s1&s2)
print(intersection)

