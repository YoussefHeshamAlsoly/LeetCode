from math import prod
def maximumProduct(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums = {ind:(abs(num), -1 if abs(num)!=num else 1) for ind, num in enumerate(nums)}
    nums = sorted(nums.values(), reverse=True)
    flag = None

    ret = nums[0][0] * nums[1][0]
    print(ret)
    
    if abs(sum([negative[1] for negative in nums[2:]])) == len (nums[2:]):
        pass
    else:
        for i in range(2, len(nums)):
            if nums[i][1] == -1:

                if ret < 0:
                    pass

            # I GIVE UPPPPPPPPPPPPPPPPPPP too lazy/stubborn to set 6 conditional statements. Shit looks ugly.

    # return 
    # return nums


# x = [1, 2, 3, 4, 10, 9, 8, 7, 6, 5]
# x = [-100,-98,-1,2,3,4]
# x = [1000,1000,1000]
x = [-100,-2,-3,-1]
print(maximumProduct(x))