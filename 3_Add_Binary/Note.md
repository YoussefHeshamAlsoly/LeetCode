# Stats
- Runtime: 9 ms Beats 16.36%
- Memory: 12.54 MB Beats 16.31%

# Code
```python []
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        def add_binary_strings(str1, str2):
            # Convert str1 to reversed list of integers
            list1 = [int(x) for x in str1]
            list1 = list1[::-1]
            if len(list1) >= 4:
                pad = [0] * (4 - len(list1) % 4)
                list1.extend(pad)
            else:
                pad = [0] * (4 - len(list1))
                list1.extend(pad)

            # Convert str2 to reversed list of integers
            list2 = [int(x) for x in str2]
            list2 = list2[::-1]
            if len(list2) >= 4:
                pad = [0] * (4 - len(list2) % 4)
                list2.extend(pad)
            else:
                pad = [0] * (4 - len(list2))
                list2.extend(pad)

            # Ensure both lists are the same length
            max_len = max(len(list1), len(list2))
            list1.extend([0] * (max_len - len(list1)))
            list2.extend([0] * (max_len - len(list2)))

            # Add binary values with carry
            answer = []
            carry = 0
            for i in range(len(list1)):
                if carry:
                    if list1[i] and list2[i]:
                        carry = 1
                        answer.append(1)
                    elif list1[i] or list2[i]:
                        carry = 1
                        answer.append(0)
                    else:
                        carry = 0
                        answer.append(1)
                else:
                    if list1[i] and list2[i]:
                        carry = 1
                        answer.append(0)
                    elif list1[i] or list2[i]:
                        carry = 0
                        answer.append(1)
                    else:
                        carry = 0
                        answer.append(0)

            # Remove trailing zero padding
            while answer[-1] == 0:
                if len(answer) == 1:
                    break
                answer.pop()

            # Convert list back to string
            final_str = ''.join(str(x) for x in answer[::-1])
            return final_str
        answer = add_binary_strings(a, b)
        return answer
```


# A "pythonic" solution

Use built-in conversion: turn both binary strings to integers with base 2, add them, and then convert the result back to a binary string by slicing off the 0b prefix.

![Flow chart](https://assets.leetcode.com/users/images/05ed8e43-941d-4eea-8d1c-67458721117e_1743689544.4302273.png)

```python []
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(int(a, 2) + int(b, 2))[2:]
```