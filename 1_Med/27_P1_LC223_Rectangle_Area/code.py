# 223. Rectangle Area
# https://leetcode.com/problems/rectangle-area/description/

# def computeArea(ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
def computeArea(ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
    left_boundary = max(ax1, bx1)
    right_boundary = min(ax2, bx2)
    
    top_boundary = min(ay2, by2)
    bottom_bondary = max(ay1, by1)
    
    
    area_1 = (ax2 - ax1)*(ay2 - ay1)
    area_2 = (bx2 - bx1)*(by2 - by1)
    
    if (left_boundary < right_boundary) and (bottom_bondary < top_boundary):
        intersection = ( right_boundary - left_boundary ) * ( top_boundary - bottom_bondary )
        
    else:
        intersection = 0
    
    return area_1 + area_2 - intersection

ax1 = -3
ay1 = 0
ax2 = 3
ay2 = 4
bx1 = 0
by1 = -1
bx2 = 9
by2 = 2

ret = computeArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2)
print(ret)