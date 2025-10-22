
from collections import Counter, defaultdict


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
    


    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dic = {}

        for i in range (len(nums)):
            val = target - nums[i]

            if val in dic:
                return [dic[val], i]
            else:
                dic[nums[i]] = i
        return []
    

    def groupAnagrams(self, str_list: list[str]) -> list[list[str]]:
        str_dict = {}

        for i in range(len(str_list)):
            if str(sorted(str_list[i])) in str_dict:
                str_dict[str(sorted(str_list[i]))].append(str_list[i])
            else:
                str_dict[str(sorted(str_list[i]))] = [str_list[i]]
        print(str_dict)

                         
        return list(str_dict.values())
    

    def groupAnagrams1(self, str_list: list[str]) -> list[list[str]]:
        dict = defaultdict(list)

        for i in str_list:
            count = [0] * 26

            for j in i:
                count[ord(j) - ord('a')] += 1
            dict[tuple(count)].append(i)
        
        return list(dict.values())



        

if __name__ == "__main__":
    cls = Solution()

    print(cls.groupAnagrams1(["act","pots","tops","cat","stop","hat"]))