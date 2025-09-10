def reverse(x: int) -> int:
    # if x < 0:
    #     return int("".join([i for i in str(x)][:0:-1]))*-1
    # else:
    #     return int("".join([i for i in str(x)][::-1]))
    # if x < 0:
    #     x = int("".join([i for i in str(x)][:0:-1]))*-1
    #     return 0 if x < (-2**31) else x
    # else:
    #     x = int("".join([i for i in str(x)][::-1]))
    #     return 0 if x > (2**31) else x

    if x < 0:
        x = int( str((abs(x)))[::-1]) * -1
        return 0 if x < (-2**31) else x
    else:
        x = int( str(x)[::-1] )
        return 0 if x > (2**31) else x


x = -123
print(reverse(x))