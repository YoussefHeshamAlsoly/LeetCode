
# https://leetcode.com/problems/
# 1037. Valid Boomerang

def isBoomerang(points):
    """
    :type points: List[List[int]]
    :rtype: bool
    """

    return False if (points[0][1] - points[1][1]) * (points[1][0] - points[2][0]) == (points[1][1] - points[2][1]) * (points[0][0] - points[1][0]) else True

    # if (points[0][1] - points[1][1]) * (points[1][0] - points[2][0]) == (points[1][1] - points[2][1]) * (points[0][0] - points[1][0]):
    #     return False
    # else:return True




    # Both solutions work with the same memory usage
    # ✅
    # check1_1 = (points[0][1] - points[1][1]) * (points[1][0] - points[2][0])
    # check1_2 = (points[1][1] - points[2][1]) * (points[0][0] - points[1][0])


    # check2_1 = (points[1][1] - points[2][1]) * (points[0][0] - points[2][0])
    # check2_2 = (points[0][1] - points[2][1]) * (points[1][0] - points[2][0])


    # check3_1 = (points[0][1] - points[1][1]) * (points[0][0] - points[2][0])
    # check3_2 = (points[0][1] - points[2][1]) * (points[0][0] - points[1][0])
    
    # if check1_1 != check1_2 and check2_1 != check2_2 and check3_1 != check3_2:
    #     return True
    # else:
    #     return False
    
    # ===============================================================================

    # ✅
    # if (points[0][1] - points[1][1]) * (points[1][0] - points[2][0]) != (points[1][1] - points[2][1]) * (points[0][0] - points[1][0]):
    #     if (points[1][1] - points[2][1]) * (points[0][0] - points[2][0]) != (points[0][1] - points[2][1]) * (points[1][0] - points[2][0]):
    #         if (points[0][1] - points[1][1]) * (points[0][0] - points[2][0]) != (points[0][1] - points[2][1]) * (points[0][0] - points[1][0]):
    #             return True
    #         else:return False
    #     else:return False
    # else:return False



points = [[0,0],[1,2],[0,1]]

print(isBoomerang(points))

