# Resources
- Time:
0ms Beats 100.00%

- Memory:
12.47MB Beats 69.68%


# Code
```python []
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        x = [i for i in s.strip().split(" ")]
        return (len(x[-1]))
```