def selfDividingNumbers(left, right):
    """
    :type left: int
    :type right: int
    :rtype: List[int]
    """
    res = []
    for current_num in range(left, right+1):

        print(current_num)
        current_num = [int(digit) for digit in str(current_num)]
        if 0 in current_num:
            print("zero division skipped")
            continue

        for i in range(len(current_num)):
            whole = (int(''.join(map(str, current_num))))
            if whole % current_num[i] != 0:
                print(f"breaking; i:{i} \tsum(current_num): {sum(current_num)} \tcurrent_num[i]: {current_num[i]}")
                break
            if i == len(current_num)-1:
                res.append(whole)
    return res

print(selfDividingNumbers(1, 22))