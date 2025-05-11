
# def looper(x):
#     if x == 0:
#         return 0
#     if x < 4:
#         return 1
    
#     flag_move = 1
#     flag = 1
#     counter_stuck = 0
#     stuck = 0


#     if x>8:
#         division = int(x/8)
#     else:
#         division = int(x/2)

#     while flag:
        
#         calc_root = int(division*division)
#         stuck = calc_root
#         print(f"calc_root: {calc_root}")
#         print(f"division: {division}")

#         if calc_root > x:
#             division -= 1
#             flag_move = 0
#             print(f"Here calc_root = {calc_root}")
#             print(f"Here flag_move = {flag_move}\n\n")
        
#         elif calc_root == x:
#             print(division)
#             flag = 0
        
#         else:
#             if (calc_root/division)<calc_root:
#                 if flag_move == 0:
#                     print(division)
#                     flag = 0
#             else:
#                 division += 1


#         if calc_root == stuck:
#             counter_stuck +=1
#             if counter_stuck > 3:
#                 return 0

# items = [9]
# for i in items:
#     print("============================= New loop =============================")
#     looper(i)


def mySqrt(x):
    left, right = 0, x
    while left<=right:
        middle = left + (right - left)//2
        square = middle * middle
        if square == x:
            return (middle)
        elif square < x:
            left = middle + 1
        else:
            right = middle - 1

    return (right)


x = [2, 4, 5, 102, 8]
for i in x:
    print(f"element={i},\t mySqrt={mySqrt(i)}")