def nthFibonacci(n: int,memo={}) -> int:
    if n in memo:
        return memo[n]
    if n==0:
        return 0
    if n==1:
        return 1
    memo[n]=nthFibonacci(n-1,memo)+nthFibonacci(n-2,memo)
    return memo[n]



print(nthFibonacci(5))