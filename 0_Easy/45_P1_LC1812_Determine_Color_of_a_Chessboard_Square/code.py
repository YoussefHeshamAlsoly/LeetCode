def squareIsWhite(coordinates:str):
    """
    :type coordinates: str
    :rtype: bool
    """
    x = sum([ord(i) for i in coordinates])
    print(x)
    return False if  x > 145 and x <161 and x%2 == 0 else True

    # return x


# coordinates = "h8"
# print (False == squareIsWhite(coordinates))

coordinates = "a1"
print (False == squareIsWhite(coordinates))

coordinates = "h3"
print (True == squareIsWhite(coordinates))


coordinates = "c7"
print (False == squareIsWhite(coordinates))

