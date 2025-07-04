def addDigits(num):
    """
    :type num: int
    :rtype: int
    """
    while int(num)>9:
        num = [int(i) for i in str(num)]
        num = sum(num)

    return num

x = 22
print(addDigits(x))
