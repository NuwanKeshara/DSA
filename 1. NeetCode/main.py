def sumOfAall(idx):
    if idx == 1:
        return 1
    else:
        return idx + sumOfAall(idx - 1)
    
# print(sumOfAall(5))

# 0, 1, 1, 2, 3, 5, 8, 13...
def fibonacci(num):
    if num <= 2:
        return num - 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)
    
# print(fibonacci(4))
total = 0

def sum(num):
    # print("hello")
    if num == 0:
        return 0
    else:
        # global total
        # total += num
        print("hello")
        return sum(num-1) 
    
# print(sum(5))
# print(total)

# 0, 1, 1, 2, 3, 5, 8, 13...
# 1, 2, 3, 4, 5, 6, 7, 8, ...
def fib(n):
    if n <= 0:
        return "input value should be greater than 0"
    if n <= 2 and n > 0:
        return n-1 
    else:
        return fib(n-1) + fib(n-2)
    

# print(fib(8))


def fibo(num):
    nums = [0] * num

    for i in range(num):
        if i > 1:
            nums[i] = nums[i-1] + nums[i-2]
        else:
            nums[i] = i
    return nums[-1]

# print(fibo(8))