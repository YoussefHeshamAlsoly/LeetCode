# 165. Compare Version Numbers
# https://leetcode.com/problems/compare-version-numbers/description/

def compareVersion(version1: str, version2: str) -> int:
    version1: list[int] = list([int(i) for i in version1.split(".")])
    version2: list[int] = list([int(i) for i in version2.split(".")])
    
    if len(version1) < len(version2):
        version1.extend([0] * (len(version2) - len(version1)))
    else:
        version2.extend([0] * (len(version1) - len(version2)))
    
    
    for i in range(len(version1)):
        if version1[i] == version2[i]:
            continue
        elif version1[i] < version2[i]:
            return -1
        else:
            return 1

    return 0


version1 = "1.02.1"
version2 = "1.10"
print(compareVersion(version1, version2))
print(compareVersion(version1, version2) == -1)