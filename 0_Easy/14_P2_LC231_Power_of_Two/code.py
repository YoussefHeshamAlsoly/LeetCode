def isPowerOfTwo(n):
    if n==0:
        return False
    elif n>2 and n%2!=0:
        return False
    elif n==1:
        return True
    while n!=1:
        n = n/2
        if n == 1:
            return True
        elif n!=int(n) or (n % 2 != 0):
            return False
    return True

print(isPowerOfTwo(5))



# Another way
# if n!=abs(n):
#     return False

# n = [int(i) for i in (bin(n)[2:])]
# if sum(n) == 1 and n[0]==1:
#     return True
# else:
#     return False