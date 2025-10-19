
from collections import Counter


class Solution:
    def hashDuplicate(self, nums: list[int]) -> bool :
        dic ={}

        for i in nums:
            if i in dic:
                return True
            dic[i] = 1
        return False
    

    def hashDuplicate2(self, nums: list[int]) -> bool:
        hashset = ()

        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False
    

    def valid_anagram(self, s: str, t: str) -> bool:
        s_hash, t_hash = {}, {}

        if len(s) != len(t):
            return False

        for i in s:
            if i in s_hash:
                s_hash[i] += 1
            else: 
                s_hash[i] = 1

        for j in t:
            if j not in s_hash:
                return False
            if j in t_hash:
                t_hash[j] += 1
            else:
                t_hash[j] = 1

        for k in s_hash:
            if k in t_hash and s_hash[k] == t_hash[k]:
                continue
            else:
                return False
        return True
    

    def valid_anagram2(self, s: str, t: str) -> bool:
        s_hash, t_hash = {}, {}

        if len(s) != len(t):
            return False
        
        for i in (len(s)):
            s_hash[s[i]] = s_hash.get(s[i], 0) + 1
            t_hash[t[i]] = t_hash.get(t[i], 0) + 1

        for c in s_hash:
            if s_hash[c] != t_hash.get(c, 0):
                return False
        return True
    

    def valid_anagram3(self, s:str, t:str) -> bool:
        return Counter(s) == Counter(t)
    

    def valid_anagram4(self, s:str, t:str) -> bool:
        return sorted(s) == sorted(t)


        