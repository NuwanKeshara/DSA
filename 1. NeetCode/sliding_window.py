class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        profit = 0
        min = prices[0]

        for i in prices:
            if min > i:
                min = i
            
            profit = max(profit, i - min)
        
        return profit
    


    def lengthOfLongestSubstring(self, s:str) -> int:
        left, right = 0, 0
        freq_map = {}
        substring, max_substring = 0, 0

        while right < len(s):

            while right < len(s) and freq_map.get(s[right],0) == 0:
                freq_map[s[right]] = 1
                right += 1
                substring += 1
            
            max_substring = max(max_substring, substring)

            while right < len(s) and freq_map.get(s[right]) != 0:
                freq_map[s[left]] -= 1
                substring -= 1
                left += 1

        return max_substring
    

    def lengthOfLongestSubstring2(self, s: str) -> int:

        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1

            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res
    

    def characterReplacement(self, s:str, k:int) -> int:
        left, right = 0, 0
        hashSet = set()
        substring = 0

        for right in range(len(s)):
            hashSet.add(s[right])

            while len(hashSet) > k + 1 :
                hashSet.remove(s[left])
                left += 1
            
            substring = max(substring, right - left + 1)
        return substring


    def characterReplacement2(self, s:str, k:int) -> int:
        left = 0
        hashMap = {}
        res = 0

        for right in range(len(s)):
            hashMap[s[right]] = 1 + hashMap.get(s[right],0)

            while ((right - left + 1) - max(hashMap.values())) > k:
                hashMap[s[left]] -= 1
                left += 1
            
            res = max(res, (right - left + 1))
        return res

                












if __name__ == "__main__":
    s = Solution()

    # print(s.lengthOfLongestSubstring2("abcabcbb"))
    print(s.characterReplacement2("AAABABB",1))