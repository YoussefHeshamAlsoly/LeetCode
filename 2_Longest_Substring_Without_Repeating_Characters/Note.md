# Not passed
unfortunatlly my code did not pass.
I did not want to get stuck on a problem for more than 15 mins, so I had to just accept this defeat and look through the answers to find something I like.
The following code has time complexity of O(n)

# Code
```python []
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = {}
        head = -1
        tail = 0
        ans = 0
        
        while tail < len(s):
            while head + 1 < len(s) and freq.get(s[head + 1], 0) == 0:
                head += 1
                freq[s[head]] = freq.get(s[head], 0) + 1
            
            ans = max(ans, head - tail + 1)
            
            if tail <= head:
                freq[s[tail]] -= 1
                tail += 1
            else:
                tail += 1
                head = tail - 1
        
        return ans
```