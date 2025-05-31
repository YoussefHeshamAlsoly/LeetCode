def reverseString(s):
    """
    :type s: List[str]
    :rtype: None Do not return anything, modify s in-place instead.
    """
    # s = s[::-1]
    s = [i for i in s[::-1]]
    print(s)

reverseString(["h", "e", "l", "l", "o"])


# def reverse_chars(chars):
#     print("Before:", id(chars))
#     chars[:] = chars[::-1]
#     print("After: ", id(chars))

# s = ['a', 'b', 'c']
# reverse_chars(s)
# print("Final:", s)
