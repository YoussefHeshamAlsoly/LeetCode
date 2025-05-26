def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    s = {c: s.count(c) for c in set(s)}
    t = {ch: t.count(ch) for ch in set(t)}
    return s == t


s = "anagram"
t = "nagaram"
print(isAnagram(s, t))