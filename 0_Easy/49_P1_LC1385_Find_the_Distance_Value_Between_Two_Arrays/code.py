def findTheDistanceValue(arr1:list, arr2:list, d:int):
    """
    :type arr1: List[int]
    :type arr2: List[int]
    :type d: int
    :rtype: int
    """

    
    res = len(arr1)
    for i in (arr1):
        for j in (arr2):
            if abs(i-j) <= d:
                res -= 1
                break

    return res

    # # This is the same idea as the code above, only refind for runtime and memory.
    # res = []
    # for INDEX_i, i in enumerate(arr1):
    #     for j in (arr2):
    #         if abs(i-j) <= d:
    #             if INDEX_i in res:
    #                 res.remove(INDEX_i)
    #             break
    #         else:
    #             if INDEX_i not in res:
    #                 res.append(INDEX_i)
    # return (len(res))

# arr1 = [4,5,8]
# arr2 = [10,9,1,8]
# d = 2

arr1 = [1,4,2,3]
arr2 = [-4,-3,6,10,20,30]
d = 3

# arr1 = [2,1,100,3]
# arr2 = [-5,-2,10,-3,7]
# d = 6

# arr1 = [-3, 10, 2, 8, 0, 10]
# arr2 = [-9, -1, -4, -9, -8]
# d = 9

print(findTheDistanceValue(arr1, arr2, d))