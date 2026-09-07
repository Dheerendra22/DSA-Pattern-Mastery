"""
Toggle bits in the given range
"""

def solution(n,L,R):
    a = (1<<R)-1
    b = (1<<(L-1))-1
    Mask = a^b
    return n^Mask


print(solution(17,2,4))