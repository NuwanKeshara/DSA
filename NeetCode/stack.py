class Solution:
    def isValid(self, s:str) -> bool:
        brckts_dic = {"(":")", "{":"}", "[":"]"}
        stack = []

        if not s:
            return False
        for i in s:
            if i in brckts_dic:
                stack.append(i)
            elif not(stack) or brckts_dic[stack.pop()] != i:
                return False
        if not stack:
            return True
        return False
        


if __name__ == "__main__":
    sol = Solution()
    
    val = sol.isValid("[]")
    print(val)