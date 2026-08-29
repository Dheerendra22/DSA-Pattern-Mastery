def findroot(num):
    if num < 2:
        return num
    left=2
    right=num//2

    while left<=right:
        mid = left+(right-left)//2
        sqr = mid*mid
        if sqr == num:
            return mid
        elif sqr > num:
            right=mid-1
        else:
            left=mid+1
        
    return right

print(findroot(3))