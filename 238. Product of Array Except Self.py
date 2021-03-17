# 238. Product of Array Except Self
# multiple the product of all left and all right


def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    total = 1
    left = []
    for x in nums:
        total = total*x
        left.append(total)

    total = 1
    right = []
    for x in reversed(nums):
        total = total*x
        right.append(total)

    res = []
    for i, x in enumerate(nums):
        print(i,x)
        if i == 0:
            res.append(right[-2])
        elif i == len(nums)-1:
            res.append(left[len(nums)-2])
        else:
            res.append(left[i-1]*right[(len(nums)-i-1-1)])
    print(left)
    print(right)
    return res

productExceptSelf([1,2,3, 4])


# to have constant space, we use res as left and build right on the fly