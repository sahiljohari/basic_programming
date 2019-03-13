import itertools

global str1, str2
str1 = "bd"
str2 = "abcd"

global dp
counter = itertools.count(1)
rows = len(str1)
columns = 1000
dp = [[-1 for n, _ in zip(counter, range(columns))] for _ in range(rows)]

# Using Recursion
def lcs_recursion(i,j):
    if i == len(str1) or j == len(str2):
        return 0
    elif str1[i] == str2[j]:
        return 1 + lcs_recursion(i+1, j+1)
    else:
        return max(lcs_recursion(i+1,j), lcs_recursion(i,j+1))
    
# Using Memoization
def lcs_dp(m, n, dp):
    if m == 0 or n == 0:
        return 0
    # if the same state has already been computed
    if dp[m-1][n-1] != -1:
        return dp[m-1][n-1]
    
    # if equal, then we store the value of the function call
    if str1[m-1] == str2[n-1]:
        dp[m-1][n-1] = 1 + lcs_dp(m-1, n-1, dp)
        return dp[m-1][n-1]
    else:
        dp[m-1][n-1] = max(lcs_dp(m, n-1, dp), lcs_dp(m-1, n, dp))
        return dp[m-1][n-1]

print("Using Recursion:", lcs_recursion(0,0))
print("Using Memoization:", lcs_dp(len(str1), len(str2), dp))