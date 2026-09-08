"""

"""
def findMissing(nums):
    Miss = len(nums)
    for i , n in enumerate(nums):
        Miss = Miss^(i^n)
    return Miss

print(findMissing([0,1,2,4]))