# 26. Smallest Change
# Question: Given an input amount of change x, write a function to determine the
# minimum number of coins required to make that amount of change.

# Recursive approach
def smallestChange(x, coins):
    if x == 0:
        return 0

    min_amount = x
    for coin in coins:
        if x - coin >= 0:
            c = smallestChange(x - coin, coins)
            min_amount = min(min_amount, c + 1)
            
    return min_amount

# Dynamic programming approach
def smallestChangeDP(x, coins):
    cache = [-1] * x
    cache[0] = 0
    
    return change(x, coins, cache)

def change(x, coins, cache):
    if x == 0:
        return 0

    min_amount = x
    for coin in coins:
        if x - coin >= 0:
            c = 0
            if cache[x - coin] >= 0:
                c = cache[x - coin]
            else:
                c = change(x - coin, coins, cache)
                cache[x-coin] = c
            
            min_amount = min(min_amount, c + 1)
            
    return min_amount

def main():
    coins = [25, 10, 5, 1]
    assert smallestChange(1, coins) == 1
    assert smallestChange(3, coins) == 3
    assert smallestChange(7, coins) == 3
    assert smallestChange(32, coins) == 4

    assert smallestChangeDP(1, coins) == 1
    assert smallestChangeDP(3, coins) == 3
    assert smallestChangeDP(7, coins) == 3
    assert smallestChangeDP(32, coins) == 4

    print("All test cases passed!")

if __name__ == "__main__":
    main()