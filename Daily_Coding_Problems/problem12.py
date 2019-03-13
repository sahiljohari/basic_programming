# There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. 
# Given N, write a function that returns the number of unique ways you can climb the staircase. 
# The order of the steps matters.
# For example, if N is 4, then there are 5 unique ways:
# 1, 1, 1, 1
# 2, 1, 1
# 1, 2, 1
# 1, 1, 2
# 2, 2

# What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? 
# For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.

# Using Recursion
def numSteps(n):
    if n == 0 or n == 1:
        return 1
    else:
        return numSteps(n-1) + numSteps(n-2)

# Using Dynamic Programming
def num_ways(n):
    if n == 0 or n == 1:
        return 1
    nums = [1, 1]

    for i in range(2,n+1):
        nums.append(nums[i-1] + nums[i-2])

    return nums[-1]

# -- For special case --

# Using Recursion
def num_ways_X(n, X):
    if n == 0:
        return 1
    total = 0
    for i in X:
        if n - i >= 0:
            total += num_ways_X(n-i, X)
    return total

# Using Dynamic Programming
def num_ways_X_dp(n, X):
    if n == 0:
        return 1
    nums = [1]

    for i in range(1, n+1):
        total = 0
        for j in X:
            if i - j >= 0:
                total += nums[i-j]
        nums.append(total)

    return nums[-1]
  

if __name__ == "__main__":
    N = [4, 5, 2, 7, -1, 8]
    X = [1, 3, 5]

    for steps in N:
        print("Test-Case: N=%d Output: %d" % (steps, num_ways(steps)))
    print("\n------Special case------\n")
    for steps in N:
        print("Test-Case: N=%d Output: %d" % (steps, num_ways_X_dp(steps, X)))
