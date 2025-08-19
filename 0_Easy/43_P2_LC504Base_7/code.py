def convertToBase7(num):
    """
    :type num: int
    :rtype: str
    """
    if num == 0:
        return "0"

    ans = []
    if num<0:
        ans.append('-')
        num = abs(num)

    while num != 0:
        ans.append(str(num%7))
        num = num // 7

    # if ans[0]=='-':
    #     ans.pop(0)
    #     ans.append('-')

    # return "".join(ans[::-1])

    if ans[0]=='-':
        ans.append('-')
        return "".join(ans[:0:-1])

        # ans.pop(0)
        # ans.append('-')

    return "".join(ans[::-1])

print(convertToBase7(-7))