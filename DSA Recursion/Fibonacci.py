def fibonacci(n, memo = {}):
    
    if n<=1:
        return n
    
    if n in memo:
        return memo[n]
    
    nth_fibo = (fibonacci(n-1, memo)+
                fibonacci(n-2, memo))
    memo[n] = nth_fibo
    return nth_fibo

print(fibonacci(int(input())))