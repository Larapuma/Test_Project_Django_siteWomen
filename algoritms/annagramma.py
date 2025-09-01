from collections import defaultdict
def isAnagram( s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    dict_count = defaultdict(int)
    for i in range(len(s)):
        dict_count[s[i]] += 1
        dict_count[t[i]] += 1
    for value in dict_count .values():
        if value % 2 != 0:
            return False
    return True

print(isAnagram("anagram","nagaram"))