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
        

class MinStack:
    __min = 2**31
    __min_stack:list[int] = []

    def __init__(self):
        self.__stack:list[int] = []
    
    def push(self, val:int) -> None:
        self.__stack.append(val)
        if MinStack.__min > val:
            MinStack.__min = val
        MinStack.__min_stack.append(MinStack.__min)

    def pop(self) -> None:
        self.__stack.pop()
        MinStack.__min_stack.pop()
    
    def top(self) -> int:
        return self.__stack[-1]

    def getMin(self) -> int:
        return MinStack.__min_stack[-1]
    


class MinStack2:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val) -> None:
        self.stack.append(val)
        self.min_stack.append(min(val, self.min_stack[-1] if self.min_stack else val))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]
    
    def getMin(self) -> int:
        return self.min_stack[-1]



if __name__ == "__main__":
    sol = Solution()
    
    val = sol.isValid("[]")
    # print(val)

    ms = MinStack2()
    print(ms.push(-1))
    print(ms.push(3))
    print(ms.push(-4))
    print(ms.getMin())
    print(ms.pop())
    print(ms.getMin())
    print(ms.top())