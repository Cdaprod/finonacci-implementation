def fib_recursive(n):
    """
    Basic recursive implementation - inefficient
    Time: O(2^n), Space: O(n) due to recursion stack
    """
    if n <= 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)

def fib_memoization(n, memo=None):
    """
    Top-down dynamic programming with memoization
    Time: O(n), Space: O(n)
    """
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
        
    memo[n] = fib_memoization(n-1, memo) + fib_memoization(n-2, memo)
    return memo[n]

def fib_tabulation(n):
    """
    Bottom-up dynamic programming with tabulation
    Time: O(n), Space: O(n)
    """
    if n <= 1:
        return n
        
    # Initialize the DP table
    dp = [0] * (n + 1)
    dp[1] = 1
    
    # Fill the table bottom-up
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]

def fib_optimized(n):
    """
    Space-optimized bottom-up approach
    Time: O(n), Space: O(1)
    """
    if n <= 1:
        return n
        
    prev2, prev1 = 0, 1
    
    for _ in range(2, n + 1):
        curr = prev1 + prev2
        prev2, prev1 = prev1, curr
    
    return prev1

# Example usage and comparison
n = 10
print(f"Recursive: {fib_recursive(n)}")
print(f"Memoization: {fib_memoization(n)}")
print(f"Tabulation: {fib_tabulation(n)}")
print(f"Optimized: {fib_optimized(n)}")