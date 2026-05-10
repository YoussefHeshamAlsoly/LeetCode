# 739. Daily Temperatures
# https://leetcode.com/problems/daily-temperatures/description/

def dailyTemperatures(temperatures: list[int]) -> list[int]:
    ans = []
    for i in range (len(temperatures)):
        counter = 1
        for j in range (i+1, len(temperatures)):
            if temperatures[j] > temperatures[i]:
                ans.append(counter)
                break
            else:
                counter += 1
            
            if j == len(temperatures)-1 and counter > 1:
                ans.append(0)
                break
    
    return ans+[0]*(len(temperatures)-len(ans))

temperatures = [97,32,43,78]
x = dailyTemperatures(temperatures)

print(x)