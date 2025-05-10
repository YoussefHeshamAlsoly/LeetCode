n = 5

# we need to find all the distinct ways we can climb up the stairs.
# we can either go 1 step at a time or 2 steps at a time.


# The problem used the word "distinct" which confused me into thinking that 2.1.1 steps is the same as 1.2.1 or 1.1.2 steps
# this confusion led to me writing code for that case as it follows


# def climbStairs(n):
#     """
#     :type n: int
#     :rtype: int
#     """
#     # n>=1 is a guarantee
#     if n==1:
#         return 1
#
#     if n%2 == 0:
#         return (n/2 + 1)
#     else:
#         return (int(n/2) + 1)


# Now if we wanted to address this problem like LeetCode wants, we'll find that the steps are a Fibonacci sequence
# so the answer could be a recursive one like the following 

# only problem is that it takes too much time when running on LeetCode

# def climbStairs(n):
#     """
#     :type n: int
#     :rtype: int
#     """
#     if n==0 or n==1:
#         return 1
#     return climbStairs(n-1) +climbStairs(n-2)


# So this is a better solution for the memory problem

def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    a = 1
    b = 2

    # the "_" is used to reduce memeory usage to a minimal since the actual iterator is useless in this case
    for _ in range (n-1):
        a, b = b, a+b
    return a
