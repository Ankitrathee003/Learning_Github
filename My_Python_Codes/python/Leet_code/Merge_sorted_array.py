nums1=[0,0,0,0,0]
nums2=[1,2,3,4,5]
m=0
n=5

for i in range (len(nums2)):
    nums1[m+i]=nums2[i]
print(nums1)
sp=m+n-1
np=m-1

def onesort(nums1,last_index):
    current=last_index
    while current-1>=0:
        if nums1[current-1]>nums1[current]:
            nums1[current-1],nums1[current]=nums1[current],nums1[current-1]
            current-=1
        else:
            current-=1
    return



while sp>0 and np>0:
    if np==sp:
        np-=1
    if nums1[np]>nums1[sp]:
        nums1[np],nums1[sp]=nums1[sp],nums1[np]
        onesort(nums1,np)
        sp-=1
    else:
        sp-=1
print(nums1)
