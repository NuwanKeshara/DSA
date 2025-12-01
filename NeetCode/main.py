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