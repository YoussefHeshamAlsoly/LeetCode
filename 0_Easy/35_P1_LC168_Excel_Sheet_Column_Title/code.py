def convertToTitle(columnNumber):
    """
    :type columnNumber: int
    :rtype: str
    """
    # print( chr((columnNumber//26) + ord("A")) + chr((columnNumber%26) + ord("A")))
    # print( [chr((i//26) + ord("A")) + chr((i%26) + ord("A")) for i in columnNumber] )
    # if columnNumber <= 26:
    #     return chr(columnNumber-1 + ord('A'))
    # else:
    #     return chr(((columnNumber)//26 + ord('A') - 1)) + chr((columnNumber-1)%26+ord('A')) #chr(((columnNumber-1)%26 + ord("A")))
    
    # return chr(columnNumber-1 + ord('A')) if columnNumber<=26 else chr(((columnNumber)//26 + ord('A') - 1)) + chr((columnNumber-1)%26+ord('A')) #chr(((columnNumber-1)%26 + ord("A")))

    # return "" if columnNumber==0 else convertToTitle((columnNumber-1)//26)+chr((columnNumber-1)%26+ord("A"))
    
    return "" if columnNumber==0 else convertToTitle((columnNumber-1)//26) + chr((columnNumber-1)%26 + ord("A"))


# x = [1, 25, 26, 27, 701]
x = 2147483647
x = 28
print(convertToTitle(x))


# x = 701
# f = lambda columnNumber:"" if columnNumber==0 else f((columnNumber-1)//26)+chr((columnNumber-1)%26+ord("A"))
# print(f(x))