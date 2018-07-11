def fib(n):
    # 0 1 1 2 3 5 8
    if n == 0 : return 0
    if n == 1 : return 1
    return fib(n-1) + fib(n-2)
# 5
# 3 4
# 1 2 2 3
# 1 0 1 0 1 1 2
# 1 0 1 0 1 1 0 1

# 6
# 4 5
# 2 3 3 4
# 0 1 1 2 1 2 2 3
# 0 1 1 0 1 1 0 1 0 1 1 2
# 0 1 1 0 1 1 0 1 0 1 1 0 1
for i in range(1,10):
    print(fib(i))
